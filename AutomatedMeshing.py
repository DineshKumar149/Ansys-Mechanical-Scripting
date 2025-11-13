lengthAxis = "X"
appliedForce = 1000
meshsize = 5
#MECH
#Entry Points
geometry = Model.Geometry
mesh = Model.Mesh
analysis = Model.Analyses[0]
solution = analysis.Solution
namedselection = Model.NamedSelections
geoparts = ExtAPI.DataModel.GeoData.Assemblies[0].Parts

mesh.ElementSize = Quantity(meshsize, 'mm')

def returnFaces(geoparts):
    faceList = []
    for part in geoparts:
        for body in part.Bodies:
            for face in body.Faces:
                faceList.append(face)
    return faceList
    
def findsurface(axis, location):
    selinfo = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    if axis == "X":
        axis = 0
    elif axis == "Y":
        axis = 1
    elif axis == "Z":
        axis = 2
    faceList = returnFaces(geoparts)
    faceCentroidAxisList = [round(face.Centroid[axis], 3) for face in faceList]
    if location == "min":
        reqFace = faceList[faceCentroidAxisList.index(min(faceCentroidAxisList))]
    elif location =="max":
        reqFace = faceList[faceCentroidAxisList.index(max(faceCentroidAxisList))]
    selinfo.Ids = [reqFace.Id]
    return selinfo
NS_FixedSupport = Model.AddNamedSelection()
NS_FixedSupport.Name = "NS_FixedSupport"
NS_FixedSupport.Location = findsurface(lengthAxis, 'min')
NS_Force = Model.AddNamedSelection()
NS_Force.Name = "NS_Force"
NS_Force.Location = findsurface(lengthAxis, 'max')
fixedsupport = analysis.AddFixedSupport()
fixedsupport.Location = NS_FixedSupport
force = analysis.AddForce()
force.Location = NS_Force
force.Magnitude.Output.DiscreteValues= [Quantity(appliedForce, 'N')]
eqvStress = solution.AddEquivalentStress()
totalDef = solution.AddTotalDeformation()
solution.Solve()

import sys
sys.path.append("D:/_Common")
from cred import mailCred

import clr
clr.AddReference('System')
import System.Net as net
import System.Net.Mail as smtp

a1 = Model.Analyses[0]
a1files = a1.AnalysisSettings.SolverFilesDirectory
a1solverfiles = a1files + 'solve.out'
a1s = a1.Solution

if a1s.ObjectState.ToString() == 'Solved':
    sub = 'Analysis Succeeded'
else:
    sub = 'Analysis Failed!'
    
warnings = ['warning 1', 'warning 2', 'warning 3']

msg = smtp.MailMessage()
msg.From = smtp.MailAddress(mailCred['sender'])
msg.To.Add(smtp.MailAddress(mailCred['receiver']))
msg.Subject = "Ansys Mechanical Status Update"

row = ""
for warning in warnings:
    row = row + """
    <tr>
        <td>{}</td>
    </tr>
    """.format(warning)
    
htmlBody = """
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
</style>
</head>
<body>
<h2>Service Alert</h2>
<p>Below are the list of warnings.</p>
<table>
    <tr>
        <th>Messages</th>
    </tr>
    %s
</table>
</body>
</html>
"""%(row)
msg.Body = htmlBody
msg.IsBodyHtml = True

files = [a1solverfiles]  # In same directory as script
for file in files:
    attachment = smtp.Attachment(file)
    msg.Attachments.Add(attachment)
    
# Log in to server and send email
client = smtp.SmtpClient('smtp.gmail.com', 587)
client.DeliveryMethod = smtp.SmtpDeliveryMethod.Network
client.UseDefaultCredentials = False
client.Credentials = net.NetworkCredential(mailCred['sender'], mailCred['password'])
client.EnableSsl = True
client.Send(msg)
