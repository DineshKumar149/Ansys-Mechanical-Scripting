Model.CoordinateSystems
Model.CoordinateSystems.Name
Model.CoordinateSystems.Activate()
cs=Model.CoordinateSystems
cs.Children
gcsys = cs.Children[0]
gcsys.Name
gcsys.Origin
gcsys.OriginX
cs1 = cs.AddCoordinateSystem()
cs1.Origin
cs1.OriginX
cs1.OriginX= Quantity(1,'m')
cs1.OriginY= Quantity(1,'m')
cs1.OriginZ= Quantity(1,'m')
selinfo=ExtAPI.SelectionManager.CurrentSelection
cs1.OriginLocation=selinfo
ns=Model.AddNamedSelection()
ns.Location=selinfo
cs1.OriginLocation=ns
cs1.OriginX= Quantity(1,'m')
cs1.XAxisData
cs1.Origin=[0.0,0.0,0.0]
cs1.PrimaryAxis
cs1.PrimaryAxis=CoordinateSystemAxisType.PositiveYAxis
cs1.PrimaryAxis
cs1.PrimaryAxisDefineBy
cs1.PrimaryAxisDefineBy=CoordinateSystemAlignmentType.GlobalY
cs1.SecondaryAxis=CoordinateSystemAxisType.NegativeZAxis
cs1.SecondaryAxisDefineBy
cs1.SecondaryAxisDefineBy=CoordinateSystemAlignmentType.GlobalY
cs1.OffsetX(0.2)
cs1.OffsetZ(Quantity(0.01,'cm'))
cs1.RotateX(2)
cs1.FlipX()
