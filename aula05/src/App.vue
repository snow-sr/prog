<script>
import SideNav from "@/components/SideNav.vue";
import ContentArea from "@/components/ContentArea.vue";
import HeaderComponent from "@/components/HeaderComponent.vue";
import FooterComponent from "@/components/FooterComponent.vue";

export default {
  components: { SideNav, ContentArea, HeaderComponent, FooterComponent },
};
</script>

<template>
  <HeaderComponent></HeaderComponent>
  <ContentArea></ContentArea>
  <SideNav></SideNav>
  <FooterComponent></FooterComponent>
</template>
