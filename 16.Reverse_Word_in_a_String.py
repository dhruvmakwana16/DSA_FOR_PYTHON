class Solution:
    def reverseWords(self, s):
        # Split string into words
        words = s.split()

        # Reverse the list
        words.reverse()

        # Join words with spaces
        return " ".join(words)

print(Solution().reverseWords("Dhruv is Software Engineer"))  # Output: "Engineer Software is Dhruv"