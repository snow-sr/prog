<script>
export default {
  props: {
    typeOfBorder: {
      type: String,
      default: "",
    },
  },
};
</script>

<template>
  <div :class="[typeOfBorder, 'block']">
    <slot></slot>
  </div>
</template>
