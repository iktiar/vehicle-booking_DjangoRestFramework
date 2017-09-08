import Vue from 'vue'
import Router from 'vue-router'
//  import Hello from '@/components/Hello'
import Home from '@/components/Home'
import RequisitionTicketForm from '@/components/requisition-ticket-form/Requisition-ticket-form'
import RequisitionTicket from '@/components/admin/requisition-ticket'
import RequisitionTickets from '@/components/admin/requisition-tickets'
import User from '@/components/admin/user'
import Users from '@/components/admin/users'
import LogIn from '@/components/auth/login'

Vue.use(Router)

export default
new Router({
    routes: [
        {
            path: '/',
            name: 'Home',
            component: Home
        },
        {
            path: '/requisition-ticket-form',
            name: 'RequisitionTicketForm',
            component: RequisitionTicketForm
        },
        {
            path: '/requisition-ticket/:ticket_id',
            name: 'RequisitionTicket',
            component: RequisitionTicket
        },
        {
            path: '/admin/requisition-tickets',
            name: 'RequisitionTickets',
            component: RequisitionTickets
        },
        {
            path: '/admin/user',
            name: 'User',
            component: User
        },
        {
            path: '/admin/users',
            name: 'Users',
            component: Users
        },
        {
            path: '/login',
            name: 'LogIn',
            component: LogIn
        }

    ]
})
