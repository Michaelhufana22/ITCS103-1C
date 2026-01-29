
user = input("Enter a word: ")

word_len = len(user)

nums = []
for x in range(word_len):
    num = int(input(f"Enter number {x + 1}: "))
    nums.append(num)

def aver(numbers):
    return sum(numbers) / len(numbers)

avs = aver(nums)

print(nums)
print("The length of the word is", word_len)
print("The average of the numbers is", avs)
if word_len > avs:
    print(f"The length of the word '{user}' is greater than the average.")
elif word_len < avs:
    print(f"The length of the word '{user}' is less than the average.")
else:
    print(f"The length of the word '{user}is equal to the average")