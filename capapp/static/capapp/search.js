const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
      return {
        results: [],
        searchQuery: null,
        page: 0,
        display: "hidden"
      }
    },
    methods: {
        startSearch: function() {
          this.page = 0
          this.results = []
          this.search()
        },
        search: function() {
            this.display = "block"
            fetch(`/search/${this.page}/${this.searchQuery}`)
            .then(response => response.json())
            .then(data => {
                this.results.push(...data.data)
            })
        },
        loadMore: function() {
            this.page++
            this.search()
        }
        // onScroll ({ target: { scrollTop, clientHeight, scrollHeight }}) {
        //     if (scrollTop + clientHeight >= scrollHeight) {
        //       this.page++
        //       this.search()
        //     }
        //   }
    },
    watch: {
      locations: function(locations){
        this.layerGroup.clearLayers()
        for(let user of locations){
          this.layerGroup.addLayer(
            L.marker([user.location__latitude, user.location__longitude])
            .bindPopup(user.username)
            .openPopup()
          )
        }
      }
    }
  }).mount("#app")