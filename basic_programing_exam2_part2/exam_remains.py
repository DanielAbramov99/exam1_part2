age: int = int(input("enter your age:"))
height: int = int(input("enter your height in cm:"))

if 8 <= age <= 18 and height > 115 or age > 18 and height > 100:
    print("you can ride on a rollercoaster:")
else:
    print("you cannot ride on a rollercoaster: ")

while True:
    number: int = int(input("enter a three digit number:"))
    num: int = int(input("enter one digit number:"))
    last_digit = number % 10
    middle_digit: int = (number // 10) % 10
    first_digit: int = number // 100
    if not 0 <= number <= 999 and 0 <= num <= 9:
        print("one of the parameters are illegal")
        continue
    else:
        if num == last_digit or num == middle_digit or num == first_digit:
            print(f"the digit is in number {True}")
        else:
            print(f"the digit is not in the number{False}")
    break

country_votes: list[int] = [0]
counter: int = 1
while True:
    try:
        print(f"country number {counter} your turn to vote:")
        vote: int = int(input("enter your vote (1 to agree, 2 to disagree, 3 to refrain and for to put a veto on: "))
        if vote > 4:
            print("illegal vote, try again")
            continue
        if vote == 4:
            country_votes.append(vote)
            print(f"the country that put veto on the vote is the {country_votes.index(4)}")
            break
        else:
            country_votes.append(vote)
            counter += 1
        if counter == 45:
            try:
                if country_votes.index(1) >= 1:
                    print(f"the first country that voted to agree is {country_votes.index(1)}")
            except ValueError:
                print(f"no country voted to agree")
                pass
            try:
                if country_votes.index(2) >= 1:
                    print(f"the first country that voted to disagree is {country_votes.index(2)}")
            except ValueError:
                print(f"no country voted to disagree")
            break
    except ValueError:
        print("illegal vote,try again")
