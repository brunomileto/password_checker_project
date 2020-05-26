# password_checker_project
###### **Python project that allow us to check if our passwords has been leaked/hacked**

###### This readme, intend to explain how all modules and functions are for and how they work

**0 - Some background information:**

    # Many many times, companies has their databases leaked. This includes big companies.
    # What happens is that those databases get leaked to the public, then, hacker can
      compile those databases, with usernames and passwords, and try to force brute loggin
      into different services.
    # There are many databases leaked that contain those information.
    # Also, there is a site called 'have i been pwned', that have a huge collection with
      those databases leaked.
    # The problem is, you can been hacked by typing your username and password on the site
      because, ideally, you are sending information to a server and that information can be
      intercepted.
    # But, this site have an API, that we can use to built a python program and make things
      secure.
    # The technique used in this program, is used by legitimate password managers like:
      "Keeper", "1Password", "Blur", etc.

0.5 - Understanding how this program work:
    
    # The website works with something called hash. So we can't actually send our password 
      in plain text. We need to convert it into a hash version.
    # A hash function will get an input and convert it into a output with fixed lenght. In other words
      the output of a hash function will have always, the same lenght and also ,for same 
      input, we will get the same output.
    # But, by using this program instead of informing our data on the website, we still 
      have the same problem. In other words, our data can be, still, intercepted when we 
      send it.
    # Even that we will send a hash version, with the output someone can guess the input and
      get our password.
    # To really solve this problem what we can do is, just send the first five characters of
      the hashed version of our password.
    # In return, we will have a list with a bunch of hashed passowords that start with the 
      same five charaters that we send, and then we can check the full hashed version of 
      our password in this list and see if it was leaked and how many times.
    # So: 
        1 - This code get's an input, that is your password.
        2 - Convert it into a hash version
        3 - Send the first five characters of the hashed version, to the website
        4 - Get a list of hashed passwords that were leaked and also, start with the same 
            first five characters that we've send
        5 - Check, in our computer, if our hashed version of our password, in in the list
            that we got from the website
        6 - Gives us a response and, if it was positive, give us how many times it was leaked
        
      
**1 - Importing modules**:

    1.1 - import requests:
        This module allow us to make requests on a website, just like a browser, but, without it
    
    1.2 - import hashlib:
        This built in module, can convert plain text into different types of hash
        
2 - Informing our data:

    2.1 - We will use the main function. It will receive the arguments that are our passwords
            and then, pass it as parameters for the function that will send the request to
            the website

3 - Step-by-step :

    3.1 - To request information we will use the function pwned_api_check.
    
    3.2 - First we need to convert the password into a hash version. For that we can use
            the hashlib that we imported
        
        3.2.1 - The way to convert a plain text into a hash, using this lib is standard and
                    can be found on its doc.
        
        3.2.2 - After converting it, we can divide it into two. The first five chars and
                    the remaining chars.
    
    3.3 - After converting it this function will call a new function "request_api_data",
            passing as parameter, the first five char variable that we've created.
    
    3.4 - This request function is simple. It gets the argument, adds it to the url of the
            API and then make a request. The return of this function is, actually the
            the response of the request. This is a list with all hashed variables that match
            with our argument
    
    3.5 - After this, we come back to our pwned_api_check function, just to return something
            The return is the call for another function, passing as parameters, the response
            of the request that we made and the remaining of our hashed password
            
    3.6 - As said, we will call another function, 'get_password_leaks_count'. This will
            convert the response into a list and do a for loop to check if something matchs
            our hashed password, and print the result!
    
                    
                    