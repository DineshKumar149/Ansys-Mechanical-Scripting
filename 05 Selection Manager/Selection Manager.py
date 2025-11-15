ExtAPI.SelectionManager
SM = ExtAPI.SelectionManager
SM.GetType
SM.CurrentSelection
SM.CurrentSelection
SM.CurrentSelection

selinfo = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selinfo
selinfo.GetType()
selinfo.Ids
selinfo.Ids = [64]
selinfo.Ids
selinfo
SM.NewSelection(selinfo)

selinfo = [91, 64, 37, 10]
selinfo.Ids
selinfo
SM.NewSelection(selinfo)

selinfo = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selinfo.Ids = [91, 64, 37, 10]
selinfo
SM.NewSelection
SM.NewSelection(selinfo)
selinfo
selinfo.Ids

selinfo = SM.CurrentSelection
selinfo
SM.NewSelection(selinfo)

SM.ClearSelection
SM.ClearSelection()

selinfo = [91, 70]
selinfo
SM.NewSelection(selinfo)

SM.SelectSameLocationX()
SM.SelectSameLocationY()
SM.SelectSameLocationY()

selinfo = SM.CurrentSelection
selinfo
SM.NewSelection(selinfo)

selinfo.Ids
selinfo.Ids = [64, 95]
SM.NewSelection(selinfo)

selinfo = SM.CurrentSelection
selinfo

pm = ExtAPI.DataModel.Project.Model.Geometry.AddPointMass()
pm.Location
pm.Location

selinfo = SM.CurrentSelection
selinfo
pm.Location = selinfo

ExtAPI.DataModel.Project.Model.Analyses[0].AddForce().Location = selinfo
