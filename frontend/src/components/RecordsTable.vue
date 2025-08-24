<template>
  <div class="records-container">
    <!-- Header -->
    <div class="header">
      <h1 class="title">
        <span class="icon">📊</span>
        Datos de Votación Exterior
      </h1>
      <p class="subtitle">Información sobre votos del exterior por país de residencia</p>
    </div>

    <!-- Search/Filter Section -->
    <SearchBar 
      :table-columns="tableColumns"
      :loading="loading"
      @filter-start="handleFilterStart"
      @filter-success="handleFilterSuccess"
      @filter-error="handleFilterError"
      @filter-clear="handleFilterClear"
    />

    <!-- Loading State -->
    <div v-if="loading" class="loading-container">
      <div class="spinner"></div>
      <p>Cargando datos...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="error-container">
      <div class="error-icon">⚠️</div>
      <h3>Error al cargar los datos</h3>
      <p>{{ error }}</p>
      <button @click="fetchData" class="retry-btn">Reintentar</button>
    </div>

    <!-- Data Table -->
    <div v-else class="table-container">
      <div class="table-header">
        <div class="table-info">
          <span class="record-count">{{ records.length }} registros encontrados</span>
        </div>
      </div>

      <div class="table-wrapper">
        <table class="data-table">
          <thead>
            <tr>
              <th v-for="column in tableColumns" :key="column.key">
                {{ column.label }}
              </th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="record in records" :key="record.id" class="table-row">
              <td v-for="column in tableColumns" :key="column.key">
                {{ record[column.key] || 'Sin datos' }}
              </td>
              <td class="actions-cell">
                <button @click="viewDetails(record)" class="action-btn view-btn">
                  👁️ Ver
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Empty State -->
      <div v-if="records.length === 0" class="empty-state">
        <div class="empty-icon">📋</div>
        <h3>No se encontraron datos</h3>
        <p>No hay registros disponibles en este momento</p>
      </div>
    </div>

    <!-- Modal para mostrar detalles -->
    <RecordDetails 
      :record="selectedRecord"
      :show-modal="showModal"
      :table-columns="tableColumns"
      @close-modal="closeModal"
    />
  </div>
</template>

<script>
import SearchBar from './SearchBar.vue'
import RecordDetails from './RecordDetails.vue'

export default {
  name: 'RecordsTable',
  components: {
    SearchBar,
    RecordDetails
  },
  data() {
    return {
      records: [],
      loading: false,
      error: null,
      tableColumns: [],
      showModal: false,
      selectedRecord: null
    }
  },
  mounted() {
    this.fetchData()
  },
  methods: {
    // Métodos para manejar eventos del SearchBar
    handleFilterStart() {
      this.loading = true
      this.error = null
    },
    
    handleFilterSuccess(data) {
      this.records = data
      this.loading = false
    },
    
    handleFilterError(errorMessage) {
      this.error = errorMessage
      this.loading = false
    },
    
    async handleFilterClear() {
      await this.fetchData()
    },
    async fetchData() {
      // Activar estado de carga
      this.loading = true
      this.error = null
      
      try {
        // Llamada al endpoint principal
        const response = await fetch('http://127.0.0.1:8000/datos')
        
        if (!response.ok) {
          throw new Error(`Error ${response.status}: ${response.statusText}`)
        }
        
        // Procesar datos JSON
        const data = await response.json()
        console.log('Datos recibidos de la API:', data)
        console.log('Número total de registros:', data.length)
        
        if (data.length > 0) {
          // Generar columnas dinámicamente del primer registro
          this.generateTableColumns(data[0])
          console.log('Columnas generadas:', this.tableColumns)
        }
        
        // Asignar datos a la tabla
        this.records = data
      } catch (err) {
        // Manejo de errores
        this.error = err.message
        console.error('Error fetching data:', err)
      } finally {
        // Desactivar loading en todos los casos
        this.loading = false
      }
    },
    
    generateTableColumns(firstRecord) {
      // Array con nombres amigables por posición
      const columnLabels = [
        "ID",                    // columna[0]
        "País Residencia",       // columna[1] 
        "Residencia",                   // columna[2]
        "Localización Residencia", 
        "Grupo Edad",               // columna[3]
        "Nivel Educativo",        // columna[4]
        "Estado Civil",        // columna[5]
        "Genero",          // columna[6]
        "Etnia",                 // columna[7]
        "Proceso Electoral",           // columna[8]
        "Oficina Inscripción",     // columna[9]
        "Puesto Votación",          // columna[10]
        "Localización",       // columna[11]
        "Año Inscripción",     // columna[12]
        "Mes Inscripcion",     // columna[13]
        "Cantidad PreInscritos",       // columna[14]
        "Cantidad Inscritos",      // columna[15]
        "Cantidad Total",      // columna[16]
                  // columna[17]
      ];
      
      // Obtener claves del primer registro
      const jsonKeys = Object.keys(firstRecord);
      
      // Mapear columnas con nombres amigables
      this.tableColumns = jsonKeys.map((key, index) => {
        // Usar nombre personalizado si existe, sino usar key original
        const customLabel = columnLabels[index];
        return {
          key: key,                   
          label: customLabel || key    
        }
      })
    },
    
    viewDetails(record) {
      // Abrir modal con registro seleccionado
      this.selectedRecord = record
      this.showModal = true
      this.$emit('view-details', record)
    },
    
    closeModal() {
      // Cerrar modal y limpiar selección
      this.showModal = false
      this.selectedRecord = null
    }
  }
}
</script>

<style src="../css/records-table.css" scoped></style>
