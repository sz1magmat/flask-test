<template>
    <div class="wrap">
      <div class="left">
        <DayPilotNavigator id="nav" :config="navigatorConfig" />
      </div>
      <div class="content">
        <DayPilotCalendar id="dp" :config="config" ref="calendar" />
      </div>
    </div>

    <div v-if="modalActive" class="modal" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Daily Schedule Information</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
          </div>
            <div class="modal-body">
              <div class="mb-3">
                <p v-for="inf in info">{{ inf }}</p>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-danger" @click="closeModal">Close</button>
            </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import {DayPilot, DayPilotCalendar, DayPilotNavigator} from '@daypilot/daypilot-lite-vue';
  import { ref } from 'vue';
  import axios from 'axios';


  export default {
    name: 'Calendar',

    data: function() {

      var date = (new Date()).toISOString().split('T')[0];
      const info = ref('');
      const modalActive = ref(false);

      const openModal = (resp) => {
        modalActive.value = true;
        info.value = resp;
      };

      const closeModal = () => {
        modalActive.value = false;
      };

      return {
        info,
        date,
        modalActive,
        closeModal,
        openModal,
        events: [],
        navigatorConfig: {
            showMonths: 3,
            skipMonths: 3,
            selectMode: "Week",
            startDate: date,
            selectionDay: date,
            onTimeRangeSelected: args => {
              this.config.startDate = args.day;
            }
        },
        config: {
            viewType: "Week",
            startDate: date,
            durationBarVisible: true,
            eventDeleteHandling: "Disabled",
            eventMoveHandling: "Disabled",
            eventResizeHandling: "Disabled",
            eventHoverHandling: "Disabled",
            eventClickHandling: "Enabled",
            eventClickHandling: "Bubble",
            onEventClick: args => {
              let resp = [];
              for (const arg in args.e.data) {
                if (arg == 'start' || arg == 'end') {
                  resp.push(arg + ': ' + args.e.data[arg].toString().split('T')[1]);
                }
              }
              //alert(resp);
              openModal(resp);
            }
        }
      }
    },
    components: {
      DayPilotCalendar,
      DayPilotNavigator,
    },
    computed: {
      calendar() {
        return this.$refs.calendar.control;
      }
    },
    methods: {
      async loadEvents() {
        const response = await axios.get('http://127.0.0.1:5000/schedule')
        let colors = ['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6', 
		                  '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
                      '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A', 
                      '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
                      '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC', 
                      '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
                      '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680', 
                      '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
                      '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3', 
                      '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF'];
        const raw_events = response.data;
        let events = []; 
        for (let i = 0; i < raw_events.length; i++) {
          let event = {
            id: raw_events[i].id,
            start: raw_events[i].start,
            end: raw_events[i].end,
            backColor: colors[Math.floor(Math.random() * 50) + 1]
          }
          events.push(event);
        }
        /*const events = [
          {
            id: 1,
            start: "2023-05-02T10:00:00",
            end: "2023-05-02T11:00:00",
            text: "Event 1",
            backColor: "#6aa84f",
            borderColor: "#38761d",
          },
          {
            id: 2,
            start: "2023-05-03T13:00:00",
            end: "2023-05-03T16:00:00",
            text: "Event 2",
            backColor: "#f1c232",
            borderColor: "#bf9000",
          },
          {
            id: 3,
            start: "2023-05-04T13:30:00",
            end: "2023-05-04T16:30:00",
            text: "Event 3",
            backColor: "#cc4125",
            borderColor: "#990000",
          }
        ];*/
        this.calendar.update({events});
      },
      
    },
    mounted() {
      this.loadEvents();
    }
  }
  </script>
  
  <style>
  .wrap {
    display: flex;
    background: #9053c7;
    background: -webkit-linear-gradient(-135deg, #c850c0, #4158d0);
    background: -o-linear-gradient(-135deg, #c850c0, #4158d0);
    background: -moz-linear-gradient(-135deg, #c850c0, #4158d0);
    background: linear-gradient(-135deg, #c850c0, #4158d0);
  }
  
  .left {
    margin-right: 10px;
  }
  
  .content {
    flex-grow: 1;
  }
  
  
  .calendar_default_event_inner {
    background: #2e78d6;
    color: white;
    border-radius: 5px;
    opacity: 0.9;
  }

  .modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}
  </style>
  