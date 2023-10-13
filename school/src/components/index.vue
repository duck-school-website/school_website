<template>
  <body>
    <h1 align="center"> {{ w }} </h1>
    <router-link to="/class">index</router-link>
    <p> {{ items }} </p>
  </body>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      items: [],
      w:"welcome to",
    }
  },
  mounted () {
    axios.get('http://127.0.0.1:8000/teacher/index/')
      .then(response => (this.items = response.data))
  },
}
</script>
