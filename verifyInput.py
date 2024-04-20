class Input:
    def __init__(self, str_in):
        str_in.replace(",", "") #retira todas as vigulas da string
        str_in.replace(";", "") #retira todas os ; da string
        str_in.replace(".", "") #retira todas os . da string
        str_in.replace("-", " ") #retira todas os - da string
        str_in.replace("_", " ") #retira todas os _ da string
        self.str = str_in.split() #separa a string em tolkiens
        self.count_words = len(self.str) #contagem de palavras
        #deixa todas as palavras em minusculo
        for wrd in self.str:
          self.str.append(wrd.lower())
          self.str.remove(wrd)
        self.str.sort()
        
    #todas as profanações da lingua portuguesa
    profanacoes = ["porra", "buceta", "caralho", "puta", "merda", "corno", "cu", "cú", "foda", "foder", "fudido", "cacete",
               "xota", "boquete", "pica", "punheta", "xoxota", "caceta", "siririca", "babaca", "broxa", "canalha",
               "escroto"]
    
    #todas as letras com acentuação da lingua portuguesa
    abc = "abcdefghijklmnopqrstuvwxyzàèìòùáéíóúýâêîôûãñõç" 
    
    #todas as vogais 
    vogais = "aeiouàèìòùáéíóúâêîôûãõ"
    
    #todas os encontros consonantais 
    encontros_consonantais = ["bl", "br", "bd", "dm", "dv", "bs", "ch", "cl", "cr", "ct", "dr", "fl", "fr", "gl", "gr",
                              "lg", "pl", "pr", "rt", "st", "tm", "tr", "tl", "vr", "lt", "sp", "xp", "cs", "ps", "pn",
                              "pt", "gn", "lh", "nh", "nf", "mp", "nt", "bj", "lm", "nd", "mb", "nj", "ns", "xm", "xt",
                              "mn", "pç", "tn", "sc", "sç", "xc", "kr", "sl", "ml", "nc", "ts", "rr", "ss", "rl"]
    
    #verifica as vogais
    def verifyVogais(self, str):
        i = -1
        count = 0
        for char in str:
            i += 1 
            #verifica se é uma consoante ou se chegou ao final
            if char not in self.vogais: 
                count = 0
                continue
            else: count += 1 #conta a recorrencia da vogal
            if count > 3: return False #se a recorrencia for maior que tres ele conta como errada
        return True
    
    #verifica as consoantes
    def verifyConsoantes(self, str):
        i = -1
        count = 0
        for char in str:
            i += 1 
            #verifica se é uma consoante ou se chegou ao final
            if char in self.vogais:
                count = 0
                continue
            else: count += 1 #conta a recorrencia da consoante
            if count == 2:
                #Se o encontro consonatal existir
                if (str[i - 1] + str[i]) not in self.encontros_consonantais: return False
                else: count = 0
        return True

    #verifica se a palavra existe
    def verifyExiste(self, str):
        if len(str) < 3: return False #verifica o tamanho da palavra
        
        for char in str:
            if char not in self.abc: return False #verifica se aquela letra exite
            if ((char + char) in str and (char + char) not in self.encontros_consonantais) or (char + char + char) in str: return False
                
        if not self.verifyVogais(str): return False #se a verificação de vogal provar que a palavra está errada
        if not self.verifyConsoantes(str): return False #se a verificação de conssoante provar que a palavra está errada
        
        return True #se tiver certo

    #verifica se a palavra é profana
    def verifyProfano(self, str):
        if str in self.profanacoes: return True
        else:  return False

    #Verifica se as palavras estão todas certas
    def verifyInput(self):
        erradas = []
        for str in self.str:
            #Verifica se a palavra existe ou se é profana
            if  self.verifyProfano(str) or not self.verifyExiste(str): 
                self.str.remove(str) #retira a palavra errada do monte
                erradas.append(str)
        return erradas