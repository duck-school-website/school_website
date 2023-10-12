<template>
  <p> {{ items }} </p>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      items: []
    }
  },
  mounted () {
    axios.get('http://127.0.0.1:8000/teacher/index/')
      .then(response => (this.items = response.data))
  },
}
</script>
