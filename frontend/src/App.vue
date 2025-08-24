
<template>
  <div id="app">
    <div class="app-container">
      <main class="main-content">
        <RecordsTable @view-details="handleViewDetails" />
      </main>
    </div>
  </div>
</template>

<script>
import RecordsTable from './components/RecordsTable.vue'

export default {
  name: 'App',
  components: {
    RecordsTable
  },
  methods: {
    handleViewDetails(record) {
      console.log('Ver detalles del registro:', record)
      // Aquí puedes implementar la lógica para mostrar los detalles
      // Por ejemplo, abrir un modal o navegar a otra vista
    }
  }
}
</script>

<style src="./css/index.css"></style>
