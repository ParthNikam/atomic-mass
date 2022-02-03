import molmass, mendeleev
from molmass import*
from mendeleev import*


print("enter a formula[CaCl2] or type 'q' to quit.")
f = str(input("\nformula: "))

while (f != 'q'):
    if (len(f) == 1 and f.isdigit()):
        break
    try:
        d = Formula(f)
        s = element(f)
        print(f"electron configuration: {s.ec}")
        print(f"electrons per shell:", end=' ')
        for i, j in s.ec.electrons_per_shell().items():
            print(f"{str(i)+ '='+ str(j)}", end=' ')
        print(f"\nelectrons: {s.electrons}")
        print(f"atomic number: {s.atomic_number}")
        print(f"empirical: {d.empirical}")
        print(f"isotope massnumber: {d.isotope.massnumber}")
        print(f"atoms: {d.atoms}\n")
        print(f"composition: \n{d.composition()}")
        f = str(input("\nformula: "))
        print()
    except:
        d = Formula(f)
        print(f"empirical: {d.empirical}")
        print(f"isotope massnumber: {d.isotope.massnumber}")
        print(f"atoms: {d.atoms}\n")
        print(f"composition: \n{d.composition()}")
        f = str(input("\nformula: "))
        print()



