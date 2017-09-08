<template>
    <div class="col-xs-12">
        <h1>Requisition tickets -admin component</h1>
        <button class="btn btn-primary" @click="fetchData">Get Data</button>
        <ul class="list-group">
            <li class="list-group-item" v-for="item in requisitionTicketLogs.messages">{{ item.requisitionTicketLog_id }} - {{ item.vehicle_type }} - {{ formatDatetime(item.from_date_time)}} - {{ formatDatetime(item.to_date_time)}} - {{ item.ticket_status }}
            <div class="btn-group">
                <button type="button" @click="edit(item.requisitionTicketLog_id)" class="btn btn-default btn-sm">
                    <span class="glyphicon glyphicon-edit"></span> Edit
                </button>
            </div>
            </li>
        </ul>
    </div>
</template>

<script>
import moment from 'moment'
export default {
    data () {
        return {
            requisitionTicketLogs: {
                requisitionTicketLog_id: '',
                type: ''
            }
        }
    },
    methods: {
        fetchData () {
            var config = { headers: {
                'Authorization': 'JWT ' + this.$store.getters.token
            }
            }
            this.$http.get('api/requisitionticket/', config).then(response => {
                return response.json()
            })
        .then(data => {
            this.requisitionTicketLogs = data
        })
        },
        formatDatetime: function (datetime) {
            if (datetime === null) {
                return '[null]'
            } else {
                return moment(datetime).format('YYYY-MM-DD, h:mm:ss a')
            }
        },
        edit: function (item) {
            this.$router.push('/requisition-ticket/' + item)
        }
    },
    created () {
        // console.log(this.$store.getters.token)
        this.fetchData()
    }

}

</script>