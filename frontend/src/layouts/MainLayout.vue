<template>
  <q-layout view="lHh Lpr lFf">
    <q-toolbar class="text-primary bg-grey-2 q-pa-lg">
      <!-- <q-img src="public/logo-placeholder.jpeg" width="80px" /> -->
      <q-toolbar-title>
        Concentual
      </q-toolbar-title>
      <div class="row items-center q-gutter-sm">
        <q-btn flat round dense>Thing1</q-btn>
        <q-btn flat round dense>Thing2</q-btn>
        <q-btn flat round dense>Thing3</q-btn>
      </div>
    </q-toolbar>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-toolbar class="text-primary bg-grey-2 q-pa-lg">
      <q-toolbar-title>Concentual 2025</q-toolbar-title>
    </q-toolbar>
  </q-layout>
</template>

<script setup lang="ts">

</script>
