# -*- coding: cp1251 -*-
string = 'An antibiotic is a type of antimicrobial substance active against bacteria. It is the most important type of antibacterial '\
    'agent for fighting bacterial infections, and antibiotic medications are widely used in the treatment and prevention of such '\
    'infections. They may either kill or inhibit the growth of bacteria. A limited number of antibiotics also possess antiprotozoal '\
    'activity. Antibiotics are not effective against viruses such as the common cold or influenza; drugs which inhibit growth of '\
    'viruses are termed antiviral drugs or antivirals rather than antibiotics. They are also not effective against fungi; drugs which '\
    'inhibit growth of fungi are called antifungal drugs. Sometimes, the term antibiotic—literally "opposing life", from the Greek '\
    'roots anti, "against" and bios, "life"—is broadly used to refer to any substance used against microbes, but in the '\
    'usual medical usage, antibiotics (such as penicillin) are those produced naturally (by one microorganism fighting another), '\
    'whereas non-antibiotic antibacterials (such as sulfonamides and antiseptics) are fully synthetic. However, both classes '\
    'have the same goal of killing or preventing the growth of microorganisms, and both are included in antimicrobial chemotherapy. '\
    '"Antibacterials" include antiseptic drugs, antibacterial soaps, and chemical disinfectants, whereas antibiotics are an '\
    'important class of antibacterials used more specifically in medicine and sometimes in livestock feed. Antibiotics have '\
    'been used since ancient times. Many civilizations used topical application of moldy bread, with many references to its '\
    'beneficial effects arising from ancient Egypt, Nubia, China, Serbia, Greece, and Rome. The first person to directly '\
    'document the use of molds to treat infections was John Parkinson (1567–1650). Antibiotics revolutionized medicine in the '\
    '20th century. Alexander Fleming (1881–1955) discovered modern day penicillin in 1928, the widespread use of which proved '\
    'significantly beneficial during wartime. However, the effectiveness and easy access to antibiotics have also led to their '\
    'overuse and some bacteria have evolved resistance to them. The World Health Organization has classified antimicrobial '\
    'resistance as a widespread "serious threat [that] is no longer a prediction for the future, it is happening right now '\
    'in every region of the world and has the potential to affect anyone, of any age, in any country". Global deaths attributable '\
    'to antimicrobial resistance numbered 1.27 million in 2019.'
string = string.lower()
string = string.replace(".", "")
string = string.replace(",", "")
string = string.replace("[", "")
string = string.replace("]", "")
string = string.replace("(", "")
string = string.replace(")", "")
string = string.replace("", " ")
string = string.replace("\"", "")
print(string)
words = set()
string_list = string.split(" ")
for word in string_list:
    words.add(word)
count_list = []
for word in words:
    count_list.append((word, string_list.count(word)))
for i in range(10):
    max = 0
    index = 0
    for word in count_list:
        if word[1] > max:
            max = word[1]
            index = count_list.index(word)
    print(count_list.pop(index))
