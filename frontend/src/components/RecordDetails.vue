<template>
  <!-- Modal para mostrar detalles -->
  <div v-if="showModal" class="modal-overlay" @click="closeModal">
    <div class="modal-container" @click.stop>
      <div class="modal-header">
        <h2 class="modal-title">
          <span class="modal-icon">📋</span>
          Detalles del Registro #{{ record?.id }}
        </h2>
        <button @click="closeModal" class="close-btn">
          <span>✕</span>
        </button>
      </div>
      
      <div class="modal-body">
        <div v-if="record" class="details-grid">
          <!-- Detalles del Registro -->
          <div class="detail-section">
            <div class="detail-items">
              <!-- Mostrar todos los campos usando tableColumns -->
              <div v-for="field in tableColumns" :key="field.key" class="detail-item">
                <span class="detail-label">{{ field.label }}:</span>
                <!-- Mostrar valor sin transformaciones -->
                <span class="detail-value">{{ record[field.key] }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="modal-footer">
        <button @click="closeModal" class="modal-close-btn">
          Cerrar
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RecordDetails',
  props: {
    record: {
      type: Object,
      default: null
    },
    showModal: {
      type: Boolean,
      default: false
    },
    tableColumns: {
      type: Array,
      default: () => []
    }
  },
  methods: {
    closeModal() {
      // Emitir evento para cerrar modal
      this.$emit('close-modal')
    }
  }
}
</script>

<style src="../css/record-details.css" scoped></style>
