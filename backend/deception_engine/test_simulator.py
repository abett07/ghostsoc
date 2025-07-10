from simulator import generate_fake_response

while True:
    attacker_input = input("Attacker command> ")
    print(generate_fake_response(attacker_input))
