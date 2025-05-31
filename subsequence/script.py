dna_1 = "ACCGTT"
dna_2 = "CCAGCA"

def longest_common_subsequence(str_1, str_2):
  print(f"Finding longest common subsequence of {str_1} and {str_2}")
  
  grid = [[0 for c in range(len(str_1) + 1)] for r in range(len(str_2) + 1)]

  for r in range(1, len(str_2) + 1):

    for c in range(1, len(str_1) + 1):

      if str_1[c - 1] == str_2[r - 1]:
        grid[r][c] = grid[r - 1][c - 1] + 1

      else:
        grid[r][c] = max(grid[r - 1][c], grid[r][c - 1])
      
  result = []

  while r> 0 and c > 0:

    if str_1[c - 1] == str_2[r - 1]:
      result.append(str_1[c - 1])
      r -= 1
      c -= 1

    elif grid[r - 1][c] > grid[r][c - 1]:
      r -= 1

    else:
      c -= 1
      
  result.reverse()
  return "".join(result)

print(longest_common_subsequence(dna_1, dna_2))