def print_head(hair, eye):
    hair_character = hair * 12

    print(hair_character)
    print(hair + "|" + format("|" + hair, ">10"))
    print(hair + "|" +format(eye, ">3"), end="")
    print(format(eye, ">3"), end="")
    print(format("|" + hair, ">4"))
    print(" |" + format("/", ">4"), end="")
    print("\\" + format("|", ">4"))
    print(" |" + format("|", ">9"))
    print(" \\" + format("'", ">3") + "--" + "'" + format("/", ">3"))
    print("   ------")

def print_body(height, arm):
    segment_neck = "     XX"
    segment_arm = arm * 4
    segment_torso = "    XXXX"
    segment_row = segment_torso + '\n'
    segment_height = segment_row * height
    print(segment_neck)
    print("#" + segment_arm + "XX" + segment_arm + "#")
    print(segment_height, end="")

def print_legs(height, shoe):
    belt = "    ===="
    leg = "  ||   ||" '\n'
    length = leg * height
    shoe_reverse = shoe[::-1]
    print(belt)
    print(length, end="")
    print(shoe + "   " + shoe_reverse)

def main():
    print('Welcome to the custom character creator tool!')
    height = int(input('Overall character height: '))
    hair = input('Character for the hair: ')
    eye = input('Character for the eyes: ')
    arm = input('Character for the arms: ')
    shoe = input('4-character string for the shoes: ')
    print()
    print_head(hair, eye)
    print_body(height, arm)
    print_legs(height, shoe)

main()