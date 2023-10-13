# Module imports
import powerfactory as pf

app = pf.GetApplication()

# Clears the output window in Digsilent
app.ClearOutputWindow()

# Activating proect
app.ActivateProject('Brazillian 7 Bus Equivalent model')

# Getting short circuit calculation object
scc = app.GetFromStudyCase('ComShc')

# Set attributes short circuit calculation
setattr(scc, 'iopt_mde', 0)      
setattr(scc, 'iopt_shc', '3psc')
setattr(scc, 'iopt_allbus', 2)   


scc.Execute()

#List of electrical buses in project
Buses = app.GetCalcRelevantObjects('.ElmTerm')

# Initialize an empty list to store Skss values
sc_power = []

for Bus in Buses:
    skss = Bus.GetAttribute('m:Skss')
    sc_power.append(skss)  

# Print the list of Skss values to output window
app.PrintPlain(sc_power)
