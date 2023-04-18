//
//  ContentView.swift
//  STUDY
//
//  Created by Ray Huang on 2023/4/19.
//

import SwiftUI

class User: Identifiable {
    let id = UUID()
    var name: String
    var nickname: String?
    var score: Int
    var scoreThisWeek: Int
    
    init(name: String, nickname: String?, score: Int, scoreThisWeek: Int) {
        self.name = name
        self.nickname = nickname
        self.score = score
        self.scoreThisWeek = scoreThisWeek
    }
}

class UserListViewModel: ObservableObject {
    @Published var users: [User] = [
        User(name: "John Doe", nickname: "JD", score: 0, scoreThisWeek: 0),
        User(name: "Jane Smith", nickname: "JS", score: 0, scoreThisWeek: 0),
        User(name: "Bob Johnson", nickname: "BJ", score: 0, scoreThisWeek: 0)
    ]
    
    func resetScores() {
        for i in 0..<users.count {
            users[i].scoreThisWeek = 0
        }
    }
}

class VotingViewModel: ObservableObject {
    @Published var votes: [String: [Double]] = [:]
    
    func vote(voterName: String, votedUserName: String, voteType: Double, photoURL: String) {
        if votes[votedUserName] == nil {
            votes[votedUserName] = []
        }
        votes[votedUserName]?.append(voteType)
    }
    
    func calculateVotes(userList: [User]) {
        for i in 0..<userList.count {
            let user = userList[i]
            if let userVotes = votes[user.name] {
                var totalVotes: Double = 0.0
                for vote in userVotes {
                    totalVotes += vote
                }
                let agreementCount = userVotes.filter({$0 == 1.0}).count
                let disagreementCount = userVotes.count - agreementCount
                if agreementCount > disagreementCount {
                    userList[i].score += Int(totalVotes)
                }
            }
        }
    }
}

struct ContentView: View {
    @ObservedObject var userListViewModel = UserListViewModel()
    @ObservedObject var votingViewModel = VotingViewModel()
    
    var body: some View {
        VStack {
            List(userListViewModel.users) { user in
                HStack {
                    Text(user.nickname ?? user.name)
                    Spacer()
                    Text("\(user.score) (\(user.scoreThisWeek))")
                }
            }
            
            Divider()
            
            VStack {
                Button("Reset scores") {
                    userListViewModel.resetScores()
                }
                
                Divider()
                
                Button("Start voting") {
                    // show the voting screen
                }
            }
        }
    }
}

struct VotingView: View {
    @ObservedObject var votingViewModel: VotingViewModel
    @State var voterName: String = ""
    @State var votedUserName: String = ""
    @State var voteType: String = "0.0"
    @State var photoURL: String = ""
    
    var body: some View {
        VStack {
            Text("Voting screen")
            
            TextField("Your name", text: $voterName)
                .textFieldStyle(RoundedBorderTextFieldStyle())
            
            TextField("Name of the person you want to vote for", text: $votedUserName)
                .textFieldStyle(RoundedBorderTextFieldStyle())
            
            Text("Vote type")
            HStack {
                Button("0.5") {
                    self.voteType = "0.5"
                }
                Button("1.0") {
                    self.voteType = "1.0"
                }
            }
            TextField("Photo URL", text: $photoURL)
                .textFieldStyle(RoundedBorderTextFieldStyle())
            
            Button("Vote") {
                votingViewModel.vote(voterName: voterName, votedUserName: votedUserName, voteType: Double(voteType)!, photoURL: photoURL)
            }
        }
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
