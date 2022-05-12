{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Select an option:\n",
      "1. Current Password\n",
      "2. Validate Current Password\n",
      "3. Set new password\n",
      "4. Check sequrity level of password\n",
      "5. Quit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The current password is: \n",
      "Dsc3$#c\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  2\n",
      "Enter the password again :  scw\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  2\n",
      "Enter the password again :  Dsc3$#c\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  3\n",
      "Enter new password: dcew\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pasword level: 0\n",
      "INVALID!\n",
      "The new password must have:\n",
      "1.Number\n",
      "2.Uppercase and lowercase character\n",
      "3.Special symbol\n",
      "4.More than 6 characters\n",
      "None\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  3\n",
      "Enter new password: SC@#$11dsq3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pasword level: 2\n",
      "Password Successfully updated!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  4\n",
      "Enter password to check its sequirity level :  dqw\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Security level of entered password is : 0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  4\n",
      "Enter password to check its sequirity level :  adef453\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Security level of entered password is : 0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  4\n",
      "Enter password to check its sequirity level :  dcVafvDASD1434\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Security level of entered password is : 1\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  4\n",
      "Enter password to check its sequirity level :  ASCascc@#%1231\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Security level of entered password is : 2\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Thank You!\n"
     ]
    }
   ],
   "source": [
    "class BasePasswordManager:\n",
    "    \n",
    "    def __init__(self):\n",
    "        self.oldPasswords = [\"Dsc3$#c\"]\n",
    "    def get_password(self):\n",
    "        return self.oldPasswords[-1]\n",
    "    def is_correct(self, passw):\n",
    "        return bool(self.oldPasswords[-1] == passw)\n",
    "    \n",
    "class PasswordManager(BasePasswordManager):\n",
    "    \n",
    "    def get_level(self, curpass):\n",
    "        rl0=\"^(?=.*[a-z])(?=.*\\d)[a-z\\d]{6,20}$\"\n",
    "        rl1=\"^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)[A-Za-z\\d]{6,20}$\"\n",
    "        rl2=\"^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$#~%&*?])[A-Za-z\\d@$#~%&*?]{6,20}$\"\n",
    "        a2=re.compile(rl2)\n",
    "        b2=re.search(rl2,curpass)\n",
    "        a1=re.compile(rl1)\n",
    "        b1=re.search(rl1,curpass)\n",
    "        a0=re.compile(rl0)\n",
    "        b0=re.search(rl0,curpass)\n",
    "        if b2:\n",
    "            return 2\n",
    "        elif b1:\n",
    "            return 1\n",
    "        elif b0:\n",
    "            return 0\n",
    "        else:\n",
    "            return 0\n",
    "    \n",
    "    def set_password(self,newpass):\n",
    "        oldPasswordLevel = self.get_level(self.oldPasswords[-1])\n",
    "        currentPasswordLevel = self.get_level(newpass)\n",
    "        \n",
    "        if currentPasswordLevel < oldPasswordLevel:\n",
    "            print(\"INVALID!\\nThe new password must have:\\n1.Number\\n2.Uppercase and lowercase character\\n3.Special symbol\\n4.More than 6 characters\")\n",
    "        else:\n",
    "            self.oldPasswords.append(newpass)\n",
    "            return \"Password Successfully updated!\"\n",
    "        \n",
    "def main():\n",
    "    a = BasePasswordManager()\n",
    "    a = PasswordManager()\n",
    "    print(\"Select an option:\\n1. Current Password\\n2. Validate Current Password\\n3. Set new password\\n4. Check sequrity level of password\\n5. Quit\")\n",
    "    \n",
    "    flag = False\n",
    "    \n",
    "    while not flag:\n",
    "        i = input(\"Enter your choice: \")\n",
    "        if i == \"1\":\n",
    "            print(\"The current password is: \")\n",
    "            print(a.get_password())\n",
    "        elif i == \"2\":\n",
    "            Password = input(\"Enter the password again : \")\n",
    "            print(a.is_correct(Password))\n",
    "        elif i == \"3\":\n",
    "            newpass = input(str(\"Enter new password:\"))\n",
    "            print(\"Pasword level: \",end=\"\")\n",
    "            print(a.get_level(newpass))\n",
    "            print(a.set_password(newpass))\n",
    "        elif i == \"4\":\n",
    "            checkLevel = input(\"Enter password to check its sequirity level : \")\n",
    "            print(\"Security level of entered password is : \",end=\"\")\n",
    "            print(a.get_level(checkLevel))\n",
    "        elif i == \"5\":\n",
    "            flag = True\n",
    "            print(\"Thank You!\")\n",
    "        else:\n",
    "            print(\"Invalid Choice!\")\n",
    "            \n",
    "if __name__==\"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
