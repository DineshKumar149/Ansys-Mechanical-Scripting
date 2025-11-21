Model.Materials.Children
m1=Model.Materials.Children[0]
m1.Activate()
m1.AssignedBodies()
m1.AssignedBodies
m1.AddMaterialAssignment()
Model.Geometry.Bodies
Model.Geometry.GetChildren(DataModelObjectCategory.Body,True)
b1=Model.Geometry.GetChildren(DataModelObjectCategory.Body,True)[0]
b1.Activate()
b1
b1.Material
b1.Material="Air"
b1.GetGeoBody()
bg1=b1.GetGeoBody()
bg1.Material
m1
b1material=bg1.Material
import materials
materials
materials.GetListMaterialProperties(b1material)
materials.GetListMaterialPropertyByName(b1material,'Density')
materials.GetMaterialPropertyByName(b1material,'Density')
materials.GetMaterialPropertyByName(b1material,'Density').GetType()
materials.GetMaterialPropertyByName(b1material,'Density')['Density']
materials.GetMaterialPropertyByName(b1material,'Density')['Density'][1]
materials.GetMaterialPropertyByName(b1material,'Thermal Conductivity')
materials.GetMaterialPropertyByName(b1material,'Thermal Conductivity')['Temperature']
materials.GetMaterialPropertyByName(b1material,'Thermal Conductivity')['Temperature'][0]
materials.GetMaterialPropertyByName(b1material,'Thermal Conductivity')['Temperature'][1]
