<script setup>
  import { ref } from 'vue'
  const data = ref(window.DATA)
</script>

<template>
  <v-app>
    <v-main>
      <p>{{ data.data }}</p>
    </v-main>
  </v-app>
</template>


