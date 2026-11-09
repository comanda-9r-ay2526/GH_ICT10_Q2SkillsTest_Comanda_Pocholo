from pyscript import display, document


def findElement(e):
    document.getElementById("output").innerHTML = " "
    element = document.getElementById("element").value

    nonmetal = { # dictionary
        'H' : ['H', 'Hydrogen', 1, 1.008],
        'He' : ['He', 'Helium', 2, 4.003],
        'C' : ['C', 'Carbon', 6, 12.011],
        'N' : ['N', 'Nitrogen', 7, 14.007],
        'O' : ['O', 'Oxygen', 8, 15.999],
        'F' : ['F', 'Fluorine', 9, 18.998],
        'Ne' : ['Ne', 'Neon', 10, 20.180],
        'P' : ['P', 'Phosphorus', 15, 30.974],
        'S' : ['S', 'Sulfur', 16, 32.066],
        'Cl' : ['Cl', 'Chlorine', 17, 35.453],
        'Ar' : ['Ar', 'Argon', 18, 39.948],
        'Se' : ['Se', 'Selenium', 34, 78.971],
        'Br' : ['Br', 'Bromine', 35, 79.904],
        'Kr' : ['Kr', 'Krypton', 36, 83.798],
        'I' : ['I', 'Iodine', 53, 126.904],
        'Xe' : ['Xe', 'Xenon', 54, 131.294],
        'At' : ['At', 'Astatine', 85, 209.987],
        'R' : ['R', 'Radon', 86, 222.018],
        'Ts' : ['Ts', 'Tennessine', 117, 294],
        'Og' : ['Og', 'Oganesson', 118, 294],
    }

    e_check = element in nonmetal # check if element entered is in dictionary
    
    display_message = (f"The element you entered is not on the list", f'{nonmetal[element]}')
    display(display_message[e_check], target="output")
