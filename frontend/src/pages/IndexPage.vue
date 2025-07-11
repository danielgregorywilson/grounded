<template>
  <q-page class="q-px-xl">
    <div class="row items-center justify-evenly q-mx-xl">
      <q-img src="public/logo-placeholder.jpeg" class="col-3" />
      <div class="text-h4 text-center q-pa-md col">
        <strong>Concentual</strong> is an online behavioral modeling service for families looking to embrace the internet while remaining in harmony with the natural world.
      </div>
    </div>

    <div class="row items-center justify-center q-my-lg">
      <q-btn class="bg-primary text-white" size="lg" @click="showSurvey = true">Interested?</q-btn>
    </div>

    <div class="bg-grey-2 q-pa-lg">
      <div class="text-h3">
        <div class="text-h5 text-center q-mb-md">
          <strong>What We Are</strong>
        </div>
        <div class="text-body1 text-center">
          We are dedicated to helping families navigate digital life with intention and balance, providing tools and guidance for healthy online habits.
        </div>
      </div>

      <div class="q-mt-lg">
        <div class="text-h5 text-center q-mb-md">
          <strong>What we Do</strong>
        </div>
        <div class="text-body1 text-center">
          We provide practical tools, personalized guidance, and educational resources to help families build healthy digital habits, set boundaries, and foster positive online experiences together.
        </div>
      </div>

      <div class="q-mt-lg">
        <div class="text-h5 text-center q-mb-md">
          <strong>Who We Are Not</strong>
        </div>
        <div class="text-body1 text-center">
          We are not here to dictate how families should use technology, but rather to offer support and resources for making informed choices.
        </div>
      </div>
    </div>

    <div class="row items-center justify-evenly q-mt-lg">  
      <q-card class="col-6 q-pa-lg">
        <q-card-section>
          <blockquote class="q-mb-none text-center">
            <em>
              "Concentual helped our family find a healthy balance with technology. The guidance and resources made a real difference in our daily lives."
            </em>
            <div class="q-mt-md text-subtitle2">
              — The Johnson Family
            </div>
          </blockquote>
        </q-card-section>
      </q-card>
      <q-img src="https://placekittens.com/200/200" class="col-3" />  
    </div>

    <div class="row items-center justify-center q-my-lg">
      <q-btn class="bg-primary text-white" size="lg" @click="showSurvey = true">Interested?</q-btn>
    </div>


    <q-dialog v-model="showSurvey">
      <q-card class="q-pa-md">
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeXLVAFRXDCNmpAtm-XY16l7O1iI9PO40lwrv2cxTGCSTAu-A/viewform?embedded=true" width="500" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
      </q-card>
    </q-dialog>

  </q-page>
</template>

<script setup lang="ts">

import { ref } from 'vue';
const showSurvey = ref(false);


</script>
