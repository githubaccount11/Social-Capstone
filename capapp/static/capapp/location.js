
const lat = document.querySelector("#id_lat")
const long = document.querySelector("#id_long")

navigator.geolocation.getCurrentPosition((position) => {
    lat.textContent = position.coords.latitude
    long.textContent = position.coords.longitude
}, err => {
    // console.error(err)
})