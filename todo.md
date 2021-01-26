LAP 4 Code Challenge

Let’s face it, most developers are a bit lazy. One thing that can be really laborious is typing in very long URL’s so let's solve that problem! You are going to create a URL shortener.

To test an existing, free, URL shortener service, check out Free URL Shortener.

You will be working in pairs for this challenge and teaming up with another pair to give feedback via PR review.

Requirements

Users should be able to enter a url into an input box on your website's front page
Your backend will then generate a shortened path at which a User can access their url
You must implement Python in some capacity in this application
Store this shortened path and it's longer counterpart in a database
No login should be required to create a shortened URL
If User tries to access your website with a path you have stored in your database, they should get rerouted to the URL it relates to
If User tries to access your website with a path you do not have stored in your database, they should get rerouted to the homepage where they can create a new short URL
Example:

User visits your site, www.short.io
User enters http://getfutureproof.co.uk/ to the provided input
User receives a new, short URL eg. www.short.io/u5o83
User can now access the futureproof site via the new, short URL