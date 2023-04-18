
STUDY
=============

IOS application. I wrote it for my classmates


# Functions

## User list

The "User list" is a feature of the app that provides a way for users to keep track of each other's scores and to view each other's real names and nicknames. The user list is implemented as a list of users, where each user has a real name, a nickname, and a score. The user list is managed by the UserListViewModel class, which provides methods to add, remove, and retrieve users.

The user list can be accessed through the UserListView, which displays a list of users as a SwiftUI List view. Each user is displayed as a NavigationLink, which leads to a UserDetailView when tapped. The UserDetailView displays the user's real name, nickname, and score, and provides a button to reset the user's score to zero.

The user list serves as the foundation for the app's social aspect, as it allows users to see each other's scores and to compete against each other. It also encourages users to use their real names and nicknames, which helps to build a sense of community among the app's users.

Overall, the "User list" feature is an essential component of the app, as it provides a way for users to connect with each other and to engage in friendly competition.

## Scores

The "Scores" feature of the app provides a way for users to keep track of their scores and to view the scores of other users. It is implemented as a User class, which represents a user in the app and includes the user's name, nickname, and score.

The score of each user is managed by the UserListViewModel class, which provides methods to retrieve and update the score of a user. The score is initially set to zero for each user, and it is reset to zero every week, as specified in the app's requirements.

The score is displayed under each user's name in the UserListView and the UserDetailView. The score is also updated when a user receives votes through the "Voting" feature, as explained in the previous answer.

The "Scores" feature encourages users to engage with the app and to compete with each other. It provides a clear indication of each user's contribution to the app, and it promotes a sense of accomplishment and satisfaction when a user's score increases.

Overall, the "Scores" feature is an important part of the app, as it motivates users to participate and engage with the app, and it provides a way to recognize and appreciate each other's contributions.

## Voting 

The "Voting" feature of the app is a way for users to vote for each other and to receive votes from other users. It is implemented as a VotingViewModel class, which manages the voting process and the list of votes.

The voting process is initiated by a user through the VotingView, where the user can select another user to vote for and choose a vote type (0.5 points or 1 point). The user can also upload a photo to support their vote. When the user submits their vote, the VotingViewModel class adds the vote to the list of votes.

The VotingView also displays the list of votes as a SwiftUI List view, with each vote displayed as a VotingRow. The VotingRow displays the voter's name, the voted user's name, the vote type, and the photo (if any). The vote list is automatically updated as new votes are added.

The VotingViewModel class calculates the votes and updates the scores of the voted users accordingly. If the number of agreeing votes among all users is greater than the number of disagreeing votes, the voting points will be added to the voted user's score. The voting points are either 0.5 or 1 point, depending on the vote type.

The "Voting" feature encourages users to engage with each other and to show appreciation for each other's contributions. It also adds an element of fun and excitement to the app, as users can compete for votes and see who receives the most votes.

Overall, the "Voting" feature is an important component of the app, as it promotes social interaction and friendly competition among users.

# (This application is now only testing version)
