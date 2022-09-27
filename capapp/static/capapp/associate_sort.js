
followingNameBtn = document.getElementById("following-name")
followingDistBtn = document.getElementById("following-distance")
followersNameBtn = document.getElementById("followers-name")
followersDistBtn = document.getElementById("followers-distance")
friendsNameBtn = document.getElementById("friends-name")
friendsDistBtn = document.getElementById("friends-distance")
followingDiv = document.getElementById("following-div")
followersDiv = document.getElementById("followers-div")
friendsDiv = document.getElementById("friends-div")
followingNameSortAscending = false
followingDistanceSortAscending = false
followersNameSortAscending = false
followersDistanceSortAscending = false
friendsNameSortAscending = false
friendsDistanceSortAscending = false

function dist(lat1, lon1, lat2, lon2) {
    if ((lat1 == lat2) && (lon1 == lon2)) {
		return 0;
	}
	else {
		var radlat1 = Math.PI * lat1/180;
		var radlat2 = Math.PI * lat2/180;
		var theta = lon1-lon2;
		var radtheta = Math.PI * theta/180;
		var dist = Math.sin(radlat1) * Math.sin(radlat2) + Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
		if (dist > 1) {
			dist = 1;
		}
		dist = Math.acos(dist);
		dist = dist * 180/Math.PI;
		dist = dist * 60 * 1.1515;
		return dist;
    }
 }

function followingNameSort(persons, followee, follower) {
    followingDiv.innerHTML = ''
    if (followingNameSortAscending == false) {
        persons.sort(function (a,b) {
            if (a.first_name + a.last_name < b.first_name + b.last_name) {
                return -1
            }
            if (a.first_name + a.last_name > b.first_name + b.last_name) {
                return 1
            }
            return 0
        })
        followingNameSortAscending = true
    } else {
        persons.reverse()
    }
    createElements(persons, followee, follower)
}

function followingDistSort(persons, followee, follower) {
    followingNameSortAscending = false
    followingDiv.innerHTML = ''
    if (followingDistanceSortAscending == false) {
        persons.sort((p1, p2) => dist(parseFloat(p1.lat), parseFloat (p1.long)) - 
        dist(parseFloat(p2.lat), parseFloat(p2.long)))

        followingDistanceSortAscending = true
    } else {
        persons.reverse()
    }
    createElements(persons, followee, follower)
}

function followersNameSort(persons, followee, follower) {
    followersDiv.innerHTML = ''
    if (followersNameSortAscending == false) {
        persons.sort(function (a,b) {
            if (a.first_name + a.last_name < b.first_name + b.last_name) {
                return -1
            }
            if (a.first_name + a.last_name > b.first_name + b.last_name) {
                return 1
            }
            return 0
        })
        followersNameSortAscending = true
    } else {
        persons.reverse()
    }
    createElements(persons, followee, follower)
}

function followersDistSort(persons, followee, follower) {
    followersNameSortAscending = false
    followersDiv.innerHTML = ''
    if (followersDistanceSortAscending == false) {
        persons.sort((p1, p2) => dist(parseFloat(p1.lat), parseFloat (p1.long)) - 
        dist(parseFloat(p2.lat), parseFloat(p2.long)))
        followersDistanceSortAscending = true
    } else {
        persons.reverse()
    }
    createElements(persons, followee, follower)
}

function friendsNameSort(persons, followee, follower) {
    friendsDiv.innerHTML = ''
    if (friendsNameSortAscending == false) {
        persons.sort(function (a,b) {
            if (a.first_name + a.last_name < b.first_name + b.last_name) {
                return -1
            }
            if (a.first_name + a.last_name > b.first_name + b.last_name) {
                return 1
            }
            return 0
        })
        friendsNameSortAscending = true
    } else {
        persons.reverse()
    }
    createElements(persons, followee, follower)
}

function friendsDistSort(persons, followee, follower) {
    friendsNameSortAscending = false
    friendsDiv.innerHTML = ''
    if (friendsDistanceSortAscending == false) {
        persons.sort((p1, p2) => dist(parseFloat(p1.lat), parseFloat (p1.long)) - 
        dist(parseFloat(p2.lat), parseFloat(p2.long)))

        friendsDistanceSortAscending = true
    } else {
        persons.reverse()
    }
    createElements(persons, followee, follower)
}

function createElements(persons, followee, follower) {
    console.log(persons)
    for (person of persons) {
        personDiv = document.createElement("div")
        personDiv.className = "mx-2"
        imageA = document.createElement("a")
        imageA.href = `${person.id}`
        image = document.createElement("img")
        image.className = "border w-24 h-24 rounded-full"
        image.src = `${person.user_profile__profile_image}`
        image.alt = `${person.first_name} ${person.last_name}'s profile picture`
        imageA.appendChild(image)
        nameA = document.createElement("a")
        nameA.href = `${person.id}`
        firstName = document.createElement("p")
        firstName.textContent = `${person.first_name}`
        lastName = document.createElement("p")
        lastName.textContent = `${person.last_name}`
        nameA.appendChild(firstName)
        nameA.appendChild(lastName)
        personDiv.appendChild(imageA)
        personDiv.appendChild(nameA)
        if (followee) {
            followingDiv.appendChild(personDiv)
        } else if (follower) {
            followersDiv.appendChild(personDiv)
        } else {
            friendsDiv.appendChild(personDiv)
        }
    }
}

function load(friends, followers, following) {
    followingNameSort(following, true, false)
    followersNameSort(followers, false, true)
    friendsNameSort(friends, false, false)
}

fetch(`/get_friends_followers_following/${user}`)
.then(response => response.json())
.then(data => {
    results = data.data
    console.log(results)
    friends = results.friends
    followers = results.followers
    following = results.following
    window.onLoad = load(friends, followers, following)
    followingNameBtn.addEventListener("click", () => followingNameSort(following, true, false))
    followingDistBtn.addEventListener("click", () => followingDistSort(following, true, false))
    followersNameBtn.addEventListener("click", () => followersNameSort(followers, false, true))
    followersDistBtn.addEventListener("click", () => followersDistSort(followers, false, true))
    friendsNameBtn.addEventListener("click", () => friendsNameSort(friends, false, false))
    friendsDistBtn.addEventListener("click", () => friendsDistSort(friends, false, false))
})