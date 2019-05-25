var socket = io()
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

var app = new Vue({
    delimiters: ['((', '))'],
    data: {
        pic: [],

    },
    methods: {
        trigger: function () {
            $.ajax('/snap', {
                method: 'GET'
            },
            )
        },
        trigger_delay: function () {
            await sleep(5000);
            this.trigger;
        },
        update: function () {
            $.getJSON('/snap', {
                method: 'POST'
            },
                this.prev)

        },
        prev: function (data) {
            this.pic = data.pic
        }
    }
},
)
socket.on('ready', app.updates)