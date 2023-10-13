<template>
  <p> {{ class_data }} </p>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      class_data:[],
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/teacher/my_class/',
      {
        params: {
          token:1,
        }
      }).then(response => (this.class_data = response.data))
  },
  m(){
    axios.post('http://127.0.0.1:8000/teacher/my_class/',
      {
        uName: 'jiayou',
        pwd: 123
      }) .then(response => (this.class_data = response.data))
  }
}
</script>
