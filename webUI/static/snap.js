var socket = io();


var app = new Vue({
    el: '#app',
    delimiters: ['((', '))'],
    data: {
        delay: 5,
        pic: "/static/images/default.jpg"
    },
    methods: {
        trigger: function () {
            $.ajax('/snap', {
                method: 'PUT',
                success: this.updateImage
            })
        },
        updateImage: function (data) {
            console.log("Updating image to" + data.pic);
            this.pic = data.pic;
        },
        save: function () {
            $.ajax("/snap", {
                method: "POST",
                data: {
                    pic: this.pic
                }
            })
        }

    }
})