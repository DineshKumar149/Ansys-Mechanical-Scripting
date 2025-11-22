GetAllSystems()
GetSystem(Name="SYS")
sys = GetSystem(Name="SYS")
sys.Name
sys.DisplayText
sys.DisplayText = "MyStructural Analysis"

sys.GetContainer(ComponentName="Engineering Data")
ed = sys.GetContainer(ComponentName="Engineering Data")

ed.GetMaterials()
ed.GetMaterial(Name="Air")
air = ed.GetMaterial(Name="Air")
air.GetProperties()

ed.GetMaterials()
ed.GetMaterial(Name="Aluminum Alloy")
aa = ed.GetMaterial(Name="Aluminum Alloy")
aa.GetProperties()

aa.GetProperty(Name="Density")
aaden = aa.GetProperty(Name="Density")
aaden.GetChartData()
aaden.GetChartData()['Density']
aaden.GetChartData()['Density']['Density']

aaden.GetData(Variables='Density')
aaden.GetData(Variables='Temperature')
aaden.GetData(Variables=['Density','Temperature'])

aaden.SetData(Variables='Density', Values='3[g cm^-3]')
aaden.SetData(Variables='Density', Values=['5[g cm^-3]', '3[g cm^-3]'])

aaden.SetData(
    Variables=['Temperature','Density'],
    Values=[
        ['20[C]','30[C]'],
        ['5[g cm^-3]','3[g cm^-3]']
    ]
)

aalas = aa.GetProperty(Name='Elasticity')
aalas.GetChartData()

aalas.GetData(Variables="Poisson's Ratio")
aalas.GetData(Variables="Young's Modulus")

aalas.SetData(Variables="Young's Modulus", Values='200[GPa]')

aa.GetProperty(Name='S-N curve')
aa.GetProperty(Name='Tensile Yield Strength')
aa.GetProperty(Name='Tensile Yield Strength').GetData(
    Variables='Tensile Yield Strength'
)

aa.DisplayName
aa.DisplayName = 'properl'
aa.Description
aa.Description = 'my properl is good'

ed
ed.CreateMaterial(Name="mymat")

mymat = ed.CreateMaterial(Name="mymat")
mymat.CreateProperty(Name="Density")

myden = mymat.CreateProperty(Name="Density")
myden.SetData(
    Variables=['Density','Temperature'],
    Values=[
        ['20000[kg m^-3]','22000[kg m^-3]'],
        ['20[C]','22[C]']
    ]
)

mymat.CreateProperty(Name="Tensile Yield Strength")
mymat.CreateProperty(Name="Elasticity")
