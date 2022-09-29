# Capstone Proposal:


### Overview

I propose an alternative social media site. Based on the Django framework the site will allow people to follow each other publicly and see public posts. The site will also allow for friending and the ability to make and see private posts. Those you follow and friend can be sorted using javascript to allow ease of search.

### Functionality

The user can register with a username and password and then fill in personal information at will and choose whether or not to display that information publicly or privately.

The main page allows the user to make posts (publicly or privately) and see their feed of those they follow and friend. Reddit style comments.

clicking on someones icon or name will allow the user to visit their profile and view their personal information and any public and/or private posts they have made depending on the relationship (publicly followed or privately friended). 

On ones own profile allows the user to view and/or edit any personal information and it's publicity as well as view their own posts. One can also edit their posts.

At the top of each page is the ability to search for people and at the bottom is a chat feature that allows users to select a friend to chat with.

### Data Model

User:
- username
- password
- first_name
- last_name

Images:
- Url

Profile:
- user
- profile image
- images
- age
- lat
- long
- phone number
- email
- gender
- work
- education
- birthday
- date joined
- friends
- followed
- following
- boolean display field for all fields except image fields

Post:
- user
- public
- private
- name
- profile image
- text content
- image
- video
- date posted
- date edited
- comments

Comments:
- user
- name
- text content
- date posted
- date edited
- comments

### Schedule

Milestone 1:
- Registration, basic profile, and basic posting.

Milestone 2:
- complete profile, posting (except maybe video posts), user search, and basic chat

Milestone 3:
- complete chat, video posting,  blocking

Milestone 4:
- privacy policy, TOS, get domain, scale, image hosting, dark mode

Milestone 5:
- Improved Nav, reporting