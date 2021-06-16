# warmup-rev

## jd-gui for reverse WarmupRev.java

**WarmupRev.java**

```javascript
import java.util.Scanner;

public class WarmupRev {
  
	public static String cold(String t) {
		return t.substring(17) + t.substring(0, 17);
	}
	
	public static String cool(String t) {
		String s = "";
		for (int i = 0; i < t.length(); i++)
			if (i % 2 == 0)
				s += (char) (t.charAt(i) + 3 * (i / 2));
			else
				s += t.charAt(i);
		return s;
	}
		
	public static String warm(String t) {
		String a = t.substring(0, t.indexOf("l") + 1);
		String t1 = t.substring(t.indexOf("l") + 1);
		String b = t1.substring(0, t1.indexOf("l") + 1);
		String c = t1.substring(t1.indexOf("l") + 1);
		return c + b + a;
	}
	
	public static String hot(String t) {
		int[] adj = {-72, 7, -58, 2, -33, 1, -102, 65, 13, -64, 
				21, 14, -45, -11, -48, -7, -1, 3, 47, -65, 3, -18, 
				-73, 40, -27, -73, -13, 0, 0, -68, 10, 45, 13};
		String s = "";
		for (int i = 0; i < t.length(); i++)
			s += (char) (t.charAt(i) + adj[i]);
		return s;
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("Let's get warmed up! Please enter the flag: ");
		String flag = in.nextLine();
		String match = "4n_3nd0th3rm1c_rxn_4b50rb5_3n3rgy";
		if (flag.length() == 33 && hot(warm(cool(cold(flag)))).equals(match))
			System.out.println("You got it!");
		else
			System.out.println("That's not correct, please try again!");
		in.close();
	}
  
}
```

from javascript can reverse it to python:
```python3

def recold(t):
    l=len(t)
    return t[l-17:]+t[:l-17]

def recool(t):
    s=''
    for i in range(len(t)):
        if i%2==0:
            s+=chr(int(ord(t[i])-3*(i/2)))
        else:
            s+=t[i]
    return s

def rehot(t):
    adj=[-72, 7, -58, 2, -33, 1, -102, 65, 13, -64,21, 14, -45, -11, -48, -7, -1, 3, 47, -65, 3, -18, -73, 40, -27, -73, -13, 0, 0, -68, 10, 45, 13]
    s=''
    for i in range(len(t)):
        s+=chr(ord(t[i])-adj[i])
    return s

x='4n_3nd0th3rm1c_rxn_4b50rb5_3n3rgy'
x=rehot(x)
a=x[x.find('l')+1:] # 1st part in def warm
t1=x[:x.find('l')+1] # 1st part in def warm
for m in range(len(t1)): #for Bruteforce in 2nd part in def warm
    b=t1[m:len(t1)]
    c=t1[0:m]
    s=a+b+c
    print(recold(recool(s)))
```

>in def warm i use bruteforce to strip it

### run it!!

![Screenshot 2021-06-16 104511](https://user-images.githubusercontent.com/85939342/122154866-12259f00-ce90-11eb-87a7-bdf293f7a015.png)

>flag{1ncr34s3_1n_3nth4lpy_0f_5y5}
