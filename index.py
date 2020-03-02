from mypackage.nan_moyenne import GestionMoyenne

students = [{"nom":"soro","notes":[10,16]},{"nom":"koffi","notes":[12,14]}]
gestion = GestionMoyenne() 
for student in students:
    notes = student["notes"]
print(notes)

moyenne = gestion.calculmean(notes)
print(moyenne)

for student in students:
    noms = students[1]["nom"]
    moyennes = students[1]
print(noms,moyenne)