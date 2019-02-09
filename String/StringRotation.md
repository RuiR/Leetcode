# String Rotation

**Problem**  
 Assume you have a method isSubString which checks if one word is a substring of another. Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 using only one call to isSubString (e.g., "waterbottle" is a rotation of" erbottlewat").

 **Hints**  
 The key point is understanding how the rotation works. There is a separating location said index c, and the string is broken into two parts, x and y, then the rotated string is yx. And **yx should be a substring of xyxy, which is S1S1**. The final point is so amazing.

 **Solution**  
 ```python3
 def isRotatedString(S1, S2):
     if len(S1) != len(S2):
         return False
     SS = S1+S1
     return isSubString(SS, S2)
 ```
