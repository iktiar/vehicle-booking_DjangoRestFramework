<template>
    <div class="container">
    <form id="vehicle-requisition"  name="vehicle-requisition" action="#">
        <h1>Vehicle Requisition</h1>
        <div v-if="requisionInfo.message" class="alert-success text-center">{{ requisionInfo.message }}</div>
        <div v-if="requisionInfo.error_message" class="alert-warning text-center text-danger">{{ requisionInfo.error_message }}</div>
        <div class="form-group">
            <label class="">Vehicle type</label>
            <select class="form-control" v-model="requisionInfo.vehicle_type" required>
                <option disabled value="" >Please select vehicle</option>
                <option>CAR</option>
                <option>MicroBus</option>
                <option>Bus</option>
            </select>
            <span>Selected: {{ requisionInfo.vehicle_type }}</span>
        </div>
        <div class="form-group">
            <label class="">Assign Vehicle (From {{vehicles.length}})</label>
            <select class="form-control" v-model="requisionInfo.vehicle_id" required>
                <option v-for="vehicle in vehicles" v-bind:value="vehicle.vehicle_id">
                    {{ vehicle.vehicle_type }} # {{ vehicle.vehicle_number }}
                </option>
            </select>
            <span>Selected: {{ requisionInfo.vehicle_id }}</span>
        </div>
        <div class="form-group">
            <label class="">Assign Driver (From {{avialable_drivers.length}})</label>
            <select class="form-control" v-model="requisionInfo.driver_id" required>
                <option v-for="driver in avialable_drivers" v-bind:value="driver.driver_id">
                    {{ driver.name }} # {{ driver.mobile }}
                </option>
            </select>
            <span>Selected: {{ requisionInfo.driver_id }}</span>
        </div>
        <div class="form-group">
            <label class="">Origin</label>
            <input class="form-control"
                   v-model="requisionInfo.origin"
                   placeholder="Origin details" required>
        </div>
        <div class="form-group">
            <label class="">Destination</label>
            <input class="form-control"
                   v-model="requisionInfo.destination"
                   placeholder="destination details" required>
        </div>
        <div class="form-group">
            <label class="">Total passenger</label>
            <input class="form-control"
                   v-model="requisionInfo.passenger_number"
                   placeholder="passenger number">
        </div>
        <div  class="form-group">
                 <label class="">Start Date time</label>
                  {{formatDatetime(requisionInfo.from_date_time)}}
                 <date-picker v-model="requisionInfo.from_date_time" required></date-picker>
        </div>
        <div  class="form-group">
                 <label class="">End Date time</label>
                 {{formatDatetime(requisionInfo.to_date_time)}}
                 <date-picker v-model="requisionInfo.to_date_time" required></date-picker>
        </div>
        <div class="form-group">
            <label class="">Set Ticket status</label>
            <select class="form-control" v-model="requisionInfo.ticket_status" required>
                <option disabled value="" >Please select status</option>
                <option>Submitted</option>
                <option>Resolved</option>
                <option>Rescheduled</option>
            </select>
        </div>
        <div class="form-group">
            <button @click="postRequisition" class="btn btn-primary"  type="button">Submit Request</button>
         </div>
     </form>
    </div>
</template>


<script>
import moment from 'moment'
export default {
    data () {
        return {
            requisionInfo: {
                vehicle_type: '',
                passenger_number: '',
                origin: '',
                destination: '',
                from_date_time: '',
                to_date_time: '',
                message: '',
                error_message: '',
                driver_id: '',
                vehicle_id: '',
                ticket_status: ''
            },
            vehicles: '',
            avialable_drivers: ''
        }
    },
    methods: {
        postRequisition () {
            this.$http.put('api/requisitionticket/' + this.$route.params.ticket_id + '/edit/', this.requisionInfo).then(response => {
                return response.json()
            }).then(data => {
                /*
                this.requisitionTicketLogs = data
                this.message = 'Thank you'
                this.error_message = ''
                */
            }, (error) => {
                /*
                this.error_message = 'Error, Please fill all information'
                this.message = ''
                */
                this.handleError(error)
            })
        },
        getRequisition () {
            this.$http.get('api/requisitionticket/' + this.$route.params.ticket_id + '/edit/').then(response => {
                return response.json()
            }).then(data => {
                this.requisionInfo = data.messages
                this.getAvailableDrivers(this.formatDatetime(this.requisionInfo.from_date_time), this.formatDatetime(this.requisionInfo.to_date_time))
                this.getAvailableVehicles(this.formatDatetime(this.requisionInfo.from_date_time), this.formatDatetime(this.requisionInfo.to_date_time))
            }, (error) => {
                this.handleError(error)
            })
        },
        getAvailableVehicles (fromDateTime, toDateTime) {
            this.$http.get('api/free-vehicles/?from_date_time=' + fromDateTime + '&to_date_time=' + toDateTime).then(response => {
                return response.json()
            }).then(data => {
                this.vehicles = data.messages
            }, (error) => {
                this.error_message = 'Error'
                this.handleError(error)
            })
        },
        getAvailableDrivers (fromDateTime, toDateTime) {
            this.$http.get('api/free-drivers/?from_date_time=' + fromDateTime + '&to_date_time=' + toDateTime).then(response => {
                return response.json()
            }).then(data => {
                this.avialable_drivers = data.messages
            }, (error) => {
                this.error_message = 'Error'
                this.handleError(error)
            })
        },
        formatDatetime: function (datetime) {
            if (datetime === null) {
                return '[null]'
            } else {
                return moment(datetime).format('YYYY-MM-DD h:mm:ss a')
            }
        }
    },
    created () {
        console.log('came')
        console.log(this.$route.params.ticket_id)
        this.getRequisition()
    }

}

</script>