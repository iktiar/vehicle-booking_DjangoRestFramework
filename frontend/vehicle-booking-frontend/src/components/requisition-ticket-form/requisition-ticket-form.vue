<template>
    <div class="container">
    <form id="vehicle-requisition"  name="vehicle-requisition">
        <h1>Vehicle Requisition</h1>
        <div v-if="message" class="alert-success text-center">{{ message }}</div>
        <div v-if="error_message" class="alert-denger text-center text-danger">{{ error_message }}</div>
        <div class="form-group">
            <label class="">Vehicle type</label>
            <select class="form-control" v-model="vehicle_type" required>
                <option disabled value="" >Please select vehicle</option>
                <option>Car</option>
                <option>MicroBus</option>
                <option>Bus</option>
            </select>
        </div>
        <div class="form-group">
            <label class="">Origin</label>
            <input class="form-control"
                   v-model="origin"
                   placeholder="Origin details" required>
        </div>
        <div class="form-group">
            <label class="">Destination</label>
            <input class="form-control"
                   v-model="destination"
                   placeholder="destination details" required>
        </div>
        <div class="form-group">
            <label class="">Total passenger</label>
            <input class="form-control"
                   v-model="passenger_number"
                   placeholder="passenger number">
        </div>
        <div  class="form-group">
                 <label class="">Start Date time</label>
                 <date-picker v-model="from_date_time" required></date-picker>
        </div>
        <div  class="form-group">
                 <label class="">End Date time</label>
                 <date-picker v-model="to_date_time" required></date-picker>
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
            vehicle_type: '',
            passenger_number: '',
            origin: '',
            destination: '',
            from_date_time: '',
            to_date_time: '',
            message: '',
            error_message: ''
        }
    },
    methods: {
        postRequisition () {
            const requisionInfo = {
                vehicle_type: this.vehicle_type,
                passenger_number: this.passenger_number,
                origin: this.origin,
                destination: this.destination,
                from_date_time: this.from_date_time,
                to_date_time: this.to_date_time
            }

            this.$http.post('api/requisitionticket/create/', requisionInfo).then(response => {
                return response.json()
            })
            .then(data => {
                this.requisitionTicketLogs = data
                this.message = 'Thank you'
                this.error_message = ''
            }, (error) => {
                this.error_message = 'Error, Please fill all information'
                this.message = ''
                this.handleError(error)
            })
        },
        formatDatetime: function (datetime) {
            if (datetime === null) {
                return '[null]'
            } else {
                return moment(datetime).format('YYYY-MM-DD, h:mm:ss a')
            }
        },
        formatDate: function (date) {
            if (date === null) {
                return '[null]'
            } else {
                return date.format('YYYY-MM-DD')
            }
        },
        formatTime: function (time) {
            if (time === null) {
                return '[null]'
            } else {
                return time.format('HH:mm:ss')
            }
        },
        onStartDatetimeChanged: function (newStart) {
            var endPicker = this.$.endPicker.control
            endPicker.minDate(newStart)
        },
        onEndDatetimeChanged: function (newEnd) {
            var startPicker = this.$.startPicker.control
            startPicker.maxDate(newEnd)
        }
    },
    created () {

    }

}

</script>