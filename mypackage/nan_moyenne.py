class GestionMoyenne:
    def __init__(self,moymin):
        self.moymin = moymin 

    def calculmean(self,notes):
        nb_notes = len(notes)
        somme = 0
        for item in notes:
            somme += item
        if nb_notes > 0 :
            moyenne = somme/nb_notes
        else:
            moyenne = 0
        return moyenne
    def is_mean(self,moyenne):
        if moyenne >= self.moymin:
            return True
        else:
            return False


#fonction script

        #texte fonction
#if is_mean(moyenne):
   #print("felicitation")
#else:
    #print("bad")


