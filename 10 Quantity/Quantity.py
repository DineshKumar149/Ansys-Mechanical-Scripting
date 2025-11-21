Quantity
Quantity('50[mm]')
Quantity('50[Nm]')
Quantity(50,'m')
Length=50
Quantity(Length,'m')
Quantity('{}[Kgm]'.format(Length))
unit='Nm'
Quantity('{}{}'.format(Length,unit))
Quantity(Length,unit)
Quantity(Length,unit).GetType()
pm=Model.Geometry.AddPointMass()
pm.Mass=Quantity('5[Kg]')
pm.Mass=Quantity('5[kg]')
pm.Mass=Quantity('5[t]')
pm.MassMomentOfInertiaX
pm.MassMomentOfInertiaX=Quantity('20[kg mm mm]')
