<template>
  <q-page class="q-px-xl">
    <div class="row items-center justify-evenly q-mx-xl">
      <q-img src="/images/logo-placeholder.png" class="col-3" />
      <div class="text-h4 text-center q-pa-md col">
        <strong>Grounded</strong> is a free online childhood development product for families that transforms a child's preferred online services into an ongoing self-directed relationship with learning, development, and community engagement.
      </div>
    </div>

    <div class="row items-center justify-center q-my-lg">
      <q-btn class="bg-primary text-white" size="lg" @click="showSurvey = true">Interested?</q-btn>
    </div>

    <div class="bg-grey-2 q-pa-lg">
      <div class="text-h3">
        <div class="text-h5 text-center q-mb-md">
          <strong>What We Do</strong>
        </div>
        <div class="text-body1 text-center">
          The internet is a valuable tool in our society- it is a fundamental utility used for work, education, and fun. However, the internet is also run by algorithms. Multiple studies [insert hyperlink to studies?] have shown the negative impact these algorithms have on our children, be it through suggesting content that is not age appropriate, misaligned with our unique values, or simply so intriguing they can’t look away (Hello, brain rot!). Our goal is not to take the fun away from the internet: we simply want to increase your child’s access to content that is also nourishing their minds, connecting more specifically with their interests, and bringing them closer to their offline communities.
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
          <strong>What We Don't Do</strong>
        </div>
        <div class="text-body1 text-center">
          Take away the treats- we’re just adding nourishing content to the table
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

    <q-img src="/images/kid-brain.jpeg" class="q-my-lg" />

    <div class="bg-grey-2 q-pa-lg q-mt-lg">
      <div class="text-h3">
        <div class="text-h5 text-center q-mb-md">
          <strong>Mission</strong>
        </div>
        <div class="text-body1 text-center">
          Grounded LLC is dedicated to fostering balanced communities by prioritizing the complex needs of children. We developed an innovative model that reshapes the technological landscape to reconnect our youth with their communities. By utilizing radical inclusionism to include diverse perspectives and actively promoting intergenerational mentorship, we strive to bring balance and belonging to the next generation.
        </div>
      </div>

      <div class="q-mt-lg">
        <div class="text-h5 text-center q-mb-md">
          <strong>Values</strong>
        </div>
        <div class="text-body1 text-center">
          <ul>
            <li>Community - Grounded is a community first organization. We believe that despite our differences, we can connect in caring about our childrens’ wellbeing.</li>
            <li>Radical Inclusionism</li>
            <li>Self-Directed Learning</li>
            <li>Free Speech</li>
            <li>Autonomy</li>
            <li>Respect</li>
            <li>Compassion</li>
            <li>Safety</li>
          </ul>
        </div>
      </div>
      
      <div class="q-mt-lg">
        <div class="text-h5 text-center q-mb-md">
          <strong>Goals</strong>
        </div>
        <div class="text-body1 text-center">
          <ul>
            <li>To increase children’s access to content that is more age appropriate and more closely aligns with their self-determined interests and community-centered values.</li>
            <li>To re-integrate the elderly population into society by creating intergenerational mentorship opportunities.</li>
            <li>To identify joint goals and across the political spectrum</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="row items-center justify-evenly q-mt-lg">  
      <q-card class="col-6 q-pa-lg">
        <q-card-section>
          <blockquote class="q-mb-none text-center">
            <em>
              "Grounded helped our family find a healthy balance with technology. The guidance and resources made a real difference in our daily lives."
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
