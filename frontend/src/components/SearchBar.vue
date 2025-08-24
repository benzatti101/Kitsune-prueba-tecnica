<template>
  <div class="search-section">
    <div class="search-container">
      <h3 class="search-title">🔍 Filtrar Registros</h3>
      <div class="search-form">
        <div class="form-group">
          <label for="column-select" class="form-label">Columna:</label>
          <select 
            id="column-select"
            v-model="filterColumn" 
            class="form-select"
            @change="clearResults"
          >
            <option value="">Seleccionar columna...</option>
            <option v-for="column in filterableColumns" :key="column.key" :value="column.key">
              {{ column.label }}
            </option>
          </select>
        </div>
        
        <div class="form-group">
          <label for="keyword-input" class="form-label">Palabra clave:</label>
          <input 
            id="keyword-input"
            v-model="filterKeyword" 
            type="text" 
            class="form-input"
            placeholder="Escribir palabra clave..."
            @keyup.enter="applyFilter"
          />
        </div>
        
        <div class="form-actions">
          <button 
            @click="applyFilter" 
            :disabled="!filterColumn || !filterKeyword || loading"
            class="filter-btn"
          >
            <span class="btn-icon">🔎</span>
            {{ loading ? 'Buscando...' : 'Filtrar' }}
          </button>
          
          <button 
            @click="clearFilter" 
            :disabled="loading"
            class="clear-btn"
          >
            <span class="btn-icon">🗑️</span>
            Limpiar
          </button>
        </div>
      </div>
      
      <div v-if="isFiltered" class="filter-status">
        <span class="filter-info">
          📊 Mostrando resultados filtrados por <strong>{{ getColumnLabel(filterColumn) }}</strong>: 
          "<strong>{{ filterKeyword }}</strong>"
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  props: {
    tableColumns: {
      type: Array,
      default: () => []
    },
    loading: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      filterColumn: '',
      filterKeyword: '',
      isFiltered: false
    }
  },
  computed: {
    filterableColumns() {
      // Excluir solo el ID de las opciones de filtrado
      return this.tableColumns.filter(column => 
        column.key !== 'id'
      )
    }
  },
  methods: {
    async applyFilter() {
      // Validar que hay columna y palabra clave
      if (!this.filterColumn || !this.filterKeyword) {
        return
      }
      
      try {
        // Construir URL del endpoint con parámetros
        const url = `http://127.0.0.1:8000/datos/especificos/filtrar?columna=${encodeURIComponent(this.filterColumn)}&palabra=${encodeURIComponent(this.filterKeyword)}`
        console.log('URL de filtrado:', url)
        
        // Emitir evento de inicio - activar loading
        this.$emit('filter-start')
        
        // Llamada HTTP al backend
        const response = await fetch(url)
        
        if (!response.ok) {
          throw new Error(`Error ${response.status}: ${response.statusText}`)
        }
        
        // Procesar respuesta JSON
        const data = await response.json()
        console.log('Datos filtrados recibidos:', data)
        
        // Actualizar estado y emitir datos al padre
        this.isFiltered = true
        this.$emit('filter-success', data)
        
        if (data.length === 0) {
          console.log('No se encontraron resultados para el filtro aplicado')
        }
        
      } catch (err) {
        // Manejo de errores
        const errorMessage = `Error al filtrar: ${err.message}`
        console.error('Error filtering data:', err)
        this.$emit('filter-error', errorMessage)
      }
    },
    
    clearFilter() {
      // Limpiar formulario y estado
      this.filterColumn = ''
      this.filterKeyword = ''
      this.isFiltered = false
      // Emitir evento para cargar datos originales
      this.$emit('filter-clear')
    },
    
    clearResults() {
      // Limpiar keyword al cambiar columna
      this.filterKeyword = ''
    },
    
    getColumnLabel(columnKey) {
      // Obtener label amigable de la columna
      const column = this.tableColumns.find(col => col.key === columnKey)
      return column ? column.label : columnKey
    }
  }
}
</script>

<style src="../css/search-bar.css" scoped></style>
