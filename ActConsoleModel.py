dm = ExtAPI.DataModel
dm.GetType()
dm.DataModelObject
dm.AnalysisList
dm.AnalysisNames
dm.AnalysisByName("4 Cubic Static Structural")
dm.AnalysisByName("4 Cubic Static Structural").Name

an = ExtAPI.DataModel.Project.Model.AddElectricAnalysis[0]
an = ExtAPI.DataModel.Project.Model.Analyses[0]
an.ObjectId

dm.AnalysisById(34).Name
dm.GeoData
dm.Tree
dm.Childrens
dm.WorkingDir

proj = ExtAPI.DataModel.Project
proj.GetType()
proj.DataModelObjectCategory
proj.Activate()
proj.AddImage()
proj.AddComment()

comm = proj.AddComment()
comm.Author
comm.Author = "Dinesh"

proj.Activate()
comm.Activate()
comm.Author = "Raunak"
comm.Activate()
comm.Text
comm.Text = "This is Analysis of 4 Cubic Static Structural"
comm.Text = "This is my \n Analysis"

proj.Activate()
proj.Author
proj.Author = "Anvi"

proj.Activate()
proj.Subject
proj.PreparedFor
proj.Subject = "Simulation"
proj.Activate()
proj.PreparedFor = "ISGEC"

proj.Activate()
proj.FirstSaved
proj.SaveProjectAfterSolution
proj.SaveProjectAfterSolution = "True"

proj.Activate()
proj.Properties
proj.VisibleProperties

comm.Activate()
comm1 = proj.AddComment()
comm.CopyTo(comm1)
comm1.Activate()

force = ExtAPI.DataModel.Project.Model.Analyses[0].AddForce()
force.CreateParameter("Magnitude")
force.RemoveParameter("Magnitude")

proj.Children
proj.GetChildren(DataModelObjectCategory.Comment, True)
proj.GetChildren(DataModelObjectCategory.Comment, False)

proj.Model.AddComment()
proj.GetChildren(DataModelObjectCategory.Comment, False)
proj.GetChildren(DataModelObjectCategory.Comment, True)

proj.GetPath()
proj.ObjectId
proj.Model

proj.AddImage()
proj.Images()
proj.Images
proj.Images[0].Name
proj.Images[1].Name

proj.Parent
Model.Parent

proj.SpecifyMetricTemperatureInKelvin()
proj.SpecifyMetricTemperatureInCelsius()

proj.UnitSystem
proj.UnitSystem = UserUnitSystemType.StandardCGS
proj.UnitSystem

type(model)
type(Model)
model.DataModelObjectCategory
Model.DataModelObjectCategory

Model.Activate()
Model.AddChart()
Model.Activate()
Model.AddComment()
Model.Activate()

Model.Figure()
Model.Figures()
Model.AddFigure()

Model.AddImage()
Model.Activate()

Model.Ambient
Model.Color
Model.GetPath()
Model.Parent
Model.Children

Model.GetChildren(DataModelObjectCategory.Geometry, False)
Model.GetChildren(DataModelObjectCategory.Part, False)
Model.GetChildren(DataModelObjectCategory.Part, True)

Model.Name
Model.Name = "My Model"

Model.RemotePoints
Model.AddRemotePoints
Model.AddRemotePoint()

Model.ClearGeneratedData()
