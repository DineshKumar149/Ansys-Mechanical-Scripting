sys = GetSystem(Name='SYS')
ed = sys.GetContainer(ComponentName='Engineering Data')

ed
ed.ImportMaterial(Name='Concrete', Source='General_Materials.xml')
ed.ImportMaterial(Name='Acetone', Source='Fluid_Materials.xml')

mymat = ed.CreateMaterial(Name='mymat')

mymat.CreateProperty(Name='Density')

mymat.CreateProperty(Name='Coefficient of Thermal Expansion', Behavior='Isotropic', Definition='Secant')

mymat.CreateProperty(Name='Elasticity', Behavior='Isotropic')

mymat.CreateProperty(Name='Uniaxial Test Data')

mymat.CreateProperty(Name='Isotropic Hardening', Definition='Multilinear')
mymat.CreateProperty(Name='Isotropic Hardening', Definition='Nonlinear', Behavior='Power Law')

mymat.IsSuppressed()
mymat.SetSuppression(True)
mymat.SetSuppression(False)

mymat.Duplicate(ed)

mymat.Delete()

mymat2 = ed.GetMaterial(Name='mymat 2')
mymat2

ed

import os
