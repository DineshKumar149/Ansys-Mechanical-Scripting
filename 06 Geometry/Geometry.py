ExtAPI.DataModel.Project.Model.Geometry
geom = ExrAPI.DataModel.Project.Model.Geomtery
geom = ExtAPI.DataModel.Project.Model.Geometry
geom.GetType()
geom.Source
geom.Type
geom.LengthUnit
geom.DisplayStyle
geom.DisplayStyle = PrototypeDisplayStyleType.BodyColor
geom.DisplayStyle = "Material"
geom.LengthX
geom.LengthY
geom.ElementControl
geom.LengthZ
geom.Volume
geom.Mass
geom.ScaleFactorValue
geom.Bodies
geom.ActiveBodies
geom.Nodes
geom.Elements
geom.Children
geom.Children.Count

for i in geom.Children:
    print(i.Name)

for i in geom.Children:
    print("__________")
    print(i.Name)
    for x in i.Geometry:
        print(x.Name)
    print("-------end")

for i in geom.Children:
    print("----------")
    for x in i.Children:
        print(x.Name)
    print("---------end")

geom.Children[4]
geom.Children[4].Children

partA = geom.Children[4]
bodyA = partA.Children[0]

bodyA.Name
geom.Children
geom.Children[4].Name
bodyA.ObjectId
ExtAPI.DataModel.GetObjectById(29)

bodyA.CoordinateSystem
bodyA.UseReferenceTemperatureByBody
bodyA.ReferenceTemperatureValue
bodyA.Material
bodyA.NonlinearEffects
bodyA.NonLinearEffects = False
bodyA.NonlinearEffects = False

Tree.Refresh()

bodyA.ThermalStrainEffects
bodyA.MomentOfInertiaIp1

geom.GetChildren(DataModelObjectCategory.Part, False)
geom.GetChildren(DataModelObjectCategory.Part, True)
geom.GetGeometry(DataModelObjectCategory.Body, True)
geom.GetChildren(DataModelObjectCategory.Body, True)
geom.GetChildren(DataModelObjectCategory.Body, False)

bodyA.SurfaceArea

bodygeoA = bodyA.GetGeoBody()
bodygeoA
bodygeoA.Faces
bodygeoA.Faces.Count
bodygeoA.Faces[0]
bodygeoA.Faces[0].Id

for face in bodygeoA.Faces:
    print(face.Id)

bodygeoA.Faces[0].SurfaceType

pm = geom.AddPointMass()
pm.Mass
pm.Mass = Quantity('400[kg]')
pm.MassMomentOfInertiaX = Quantity('200[kg mm mm]')
pm.Location
dir(pm)

bodyA.Suppressed
bodyA.Suppressed = True
bodyA.ObjectState
