# Sistema de Backup Comprensivo

## Descripción General

El nuevo sistema de backup **captura literalmente cada ajuste** que cada categoría de optimización va a modificar, ANTES de aplicar cualquier cambio.

## ¿Qué Captura el Backup?

### 1. Valores del Registro
Para CADA comando `reg add` o `Reg.exe add`:
- **Lee el valor ACTUAL** del registro antes de modificarlo
- **Guarda**: Clave, nombre del valor, tipo, y dato actual
- **Crea archivo .REG** con todos los valores originales para restauración fácil

### 2. Estado de Servicios
Para CADA comando `sc config` o `sc stop/start`:
- **Lee la configuración ACTUAL** del servicio
- **Guarda**: Tipo de inicio actual (Automático/Manual/Deshabilitado)
- **Guarda**: Estado actual (En ejecución/Detenido)
- **Crea script .BAT** para restaurar servicios automáticamente

### 3. Configuraciones de Red
Para CADA comando `netsh`:
- **Captura el estado ACTUAL** de TCP/IP
- **Guarda**: Configuraciones globales de red
- **Guarda**: Estados de interfaces
- **Documenta**: Todo en archivo de texto para referencia

## Estructura del Backup

Cada vez que se aplica una categoría de optimización, se crea:

```
backup_{categoría}_{timestamp}/
├── {categoría}_registry_backup.reg    # Archivo .REG con TODOS los valores actuales
├── backup_metadata.json               # Metadatos completos de cada ajuste
├── restore_services.bat               # Script para restaurar servicios
└── netsh_state.txt                    # Estado completo de red
```

### Ejemplo de backup_metadata.json

```json
{
  "category": "network",
  "timestamp": "20251202_191400",
  "parsed_commands": 263,
  "backed_up_items": 156,
  "registry_values": [
    {
      "key": "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\ServiceProvider",
      "value_name": "LocalPriority",
      "current_type": "REG_DWORD",
      "current_data": "4",
      "new_type": "REG_DWORD",
      "new_data": "4"
    },
    ...
  ],
  "service_states": [
    {
      "service": "Dhcp",
      "current_start_type": "AUTO_START",
      "current_state": "RUNNING",
      "new_start_type": "auto"
    },
    ...
  ],
  "netsh_states": [
    {
      "command": "netsh int tcp set global autotuninglevel=normal",
      "current_state": "... configuración actual completa ..."
    },
    ...
  ]
}
```

## Funcionamiento

### Antes de Aplicar Optimizaciones

1. **Análisis**: El sistema lee TODOS los comandos que se van a ejecutar
2. **Extracción**: Identifica qué registro/servicio/configuración se va a modificar
3. **Lectura**: Lee el valor ACTUAL del sistema
4. **Guardado**: Guarda el valor actual en múltiples formatos:
   - Archivo .REG (restauración automática)
   - JSON (referencia y análisis)
   - Scripts .BAT (restauración de servicios)
   - Archivos .TXT (documentación)

### Durante la Aplicación

El sistema informa el progreso:
```
Creating comprehensive backup for network...
Backup created: 156 items backed up
Backup directory: backup_network_20251202_191400
Applying network optimizations...
Network optimizations completed!
```

### Restauración

#### Método 1: Automático (Registro)
```bash
reg import backup_network_20251202_191400\network_registry_backup.reg
```

#### Método 2: Automático (Servicios)
```bash
backup_network_20251202_191400\restore_services.bat
```

#### Método 3: Manual
Revisar `backup_metadata.json` para ver EXACTAMENTE qué se cambió y restaurar manualmente si es necesario.

## Diferencias con el Sistema Anterior

### Sistema Anterior ❌
- Respaldaba solo 6-9 claves principales del registro por categoría
- No capturaba valores individuales, solo exportaba árboles completos
- No guardaba estado de servicios
- No documentaba configuraciones de red
- Backup "vacío" sin valores reales

### Sistema Nuevo ✅
- Captura CADA ajuste individual que se va a modificar
- Lee el valor ACTUAL antes de modificar
- Guarda estado completo de servicios (tipo de inicio + estado)
- Documenta configuraciones de red antes y después
- Backup completo con valores literales del sistema

## Ejemplo Comparativo

### Categoría Network (263 comandos)

**Antes:**
- 6 claves de registro exportadas
- ~100 valores sin capturar
- Sin estado de servicios de red
- Sin documentación de netsh

**Ahora:**
- ~150+ valores del registro capturados individualmente
- Estado completo de servicios de red (Dhcp, Dnscache, etc.)
- Configuración completa de TCP/IP documentada
- Cada comando analizado y su impacto guardado

## Verificación

Para verificar que un backup es comprensivo, revisar:

1. **backup_metadata.json**: 
   - `parsed_commands` debe ser igual al número de comandos en la categoría
   - `backed_up_items` debe ser > 0 y significativo

2. **{categoría}_registry_backup.reg**:
   - Debe contener múltiples entradas
   - Cada entrada debe tener un valor específico

3. **restore_services.bat**:
   - Debe listar servicios con sus tipos de inicio actuales

## Implementación Técnica

El sistema usa `backup_mgr_comprehensive.py` que:

1. **Parse cada comando** para entender qué modifica
2. **Llama a Windows APIs** para leer valores actuales:
   - `reg query` para registro
   - `sc qc` para configuración de servicios
   - `sc query` para estado de servicios
   - `netsh` para configuraciones de red
3. **Guarda en múltiples formatos** para máxima flexibilidad
4. **Valida** que los datos se guardaron correctamente

## Notas Importantes

- El backup se crea **ANTES** de aplicar cualquier optimización
- Si el backup falla, las optimizaciones NO se aplican
- Cada backup tiene timestamp único, múltiples backups pueden coexistir
- Los archivos .REG usan formato UTF-16 LE para compatibilidad con Windows
- Los scripts .BAT restauran servicios a su estado original

## Soporte para Restauración Futura

Futuras versiones podrían agregar:
- Restauración automática completa desde GUI
- Comparación antes/después de optimizaciones
- Rollback selectivo de ajustes individuales
- Historial de backups con análisis de cambios
