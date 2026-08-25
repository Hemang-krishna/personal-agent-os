-- ==============================================================================
-- 7THEORY (DETAIL.7) DEDICATED SUPABASE POSTGRESQL DATABASE SCHEMA
-- Project: 7Theory Advanced PPF & Ceramic Detailing Protocol Studio
-- ==============================================================================

-- 1. STAGE INQUIRIES & CUSTOMER BOOKING LEADS TABLE
CREATE TABLE IF NOT EXISTS public.theory_bookings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_name TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    email_address TEXT,
    vehicle_make_model TEXT NOT NULL,
    vehicle_year INT,
    selected_tier TEXT NOT NULL DEFAULT 'Theory-7 Full Protocol',
    requested_stages TEXT[] DEFAULT ARRAY['01-Diagnosis', '02-Decontamination', '03-Correction', '04-Precision Fit', '05-Application', '06-Ceramic Layering', '07-Certification'],
    preferred_date DATE,
    custom_notes TEXT,
    status TEXT NOT NULL DEFAULT 'Pending Protocol Diagnosis',
    created_at TIMESTAMPTZ DEFAULT now()
);

-- 2. VEHICLE PROTOCOL AUDIT & 7-STAGE PROGRESSION LOGS TABLE (Radical Transparency)
CREATE TABLE IF NOT EXISTS public.theory_vehicle_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    booking_id UUID REFERENCES public.theory_bookings(id) ON DELETE CASCADE,
    vin_or_plate TEXT NOT NULL,
    vehicle_title TEXT NOT NULL,
    stage_number INT NOT NULL CHECK (stage_number BETWEEN 1 AND 7),
    stage_name TEXT NOT NULL,
    stage_status TEXT NOT NULL DEFAULT 'In Progress',
    inspection_notes TEXT,
    paint_depth_microns NUMERIC,
    defect_map_json JSONB DEFAULT '{}'::jsonb,
    technician_name TEXT,
    logged_media_urls TEXT[],
    completed_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- 3. CERTIFIED WARRANTY & AFTERCARE REGISTRATIONS TABLE
CREATE TABLE IF NOT EXISTS public.theory_certifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    certificate_number TEXT UNIQUE NOT NULL,
    vehicle_vin TEXT NOT NULL,
    owner_name TEXT NOT NULL,
    applied_protocol TEXT NOT NULL,
    ppf_warranty_years INT NOT NULL DEFAULT 10,
    ceramic_warranty_years INT NOT NULL DEFAULT 5,
    annual_inspection_due DATE,
    qr_verification_url TEXT,
    issue_date DATE DEFAULT CURRENT_DATE,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- 4. ANNUAL CERAMIC MEMBERSHIP & SUBSCRIPTION VAULT TABLE
CREATE TABLE IF NOT EXISTS public.theory_memberships (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    member_name TEXT NOT NULL,
    member_email TEXT NOT NULL,
    member_phone TEXT NOT NULL,
    plan_tier TEXT NOT NULL DEFAULT 'Apex Annual Ceramic Top-Up & QC ($79/mo)',
    status TEXT NOT NULL DEFAULT 'Active',
    next_service_date DATE,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- 5. CLASSIFIEDS & BESPOKE DETAILED VEHICLE SHOWCASE TABLE
CREATE TABLE IF NOT EXISTS public.theory_classifieds (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    vehicle_title TEXT NOT NULL,
    vehicle_price TEXT NOT NULL,
    specs_summary TEXT NOT NULL,
    protection_package_applied TEXT NOT NULL,
    image_url TEXT,
    contact_phone TEXT,
    is_featured BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- ENABLE ROW LEVEL SECURITY (RLS)
ALTER TABLE public.theory_bookings ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.theory_vehicle_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.theory_certifications ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.theory_memberships ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.theory_classifieds ENABLE ROW LEVEL SECURITY;

-- ALLOW PUBLIC INSERTS & SELECTS FOR LIVE STUDIO OPERATION
DO $$ BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE tablename = 'theory_bookings' AND policyname = 'Allow public insert on theory_bookings') THEN
        CREATE POLICY "Allow public insert on theory_bookings" ON public.theory_bookings FOR INSERT WITH CHECK (true);
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE tablename = 'theory_bookings' AND policyname = 'Allow public read on theory_bookings') THEN
        CREATE POLICY "Allow public read on theory_bookings" ON public.theory_bookings FOR SELECT USING (true);
    END IF;

    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE tablename = 'theory_vehicle_logs' AND policyname = 'Allow public read on theory_vehicle_logs') THEN
        CREATE POLICY "Allow public read on theory_vehicle_logs" ON public.theory_vehicle_logs FOR ALL USING (true) WITH CHECK (true);
    END IF;

    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE tablename = 'theory_certifications' AND policyname = 'Allow public read on theory_certifications') THEN
        CREATE POLICY "Allow public read on theory_certifications" ON public.theory_certifications FOR ALL USING (true) WITH CHECK (true);
    END IF;

    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE tablename = 'theory_memberships' AND policyname = 'Allow public insert on theory_memberships') THEN
        CREATE POLICY "Allow public insert on theory_memberships" ON public.theory_memberships FOR ALL USING (true) WITH CHECK (true);
    END IF;

    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE tablename = 'theory_classifieds' AND policyname = 'Allow public read on theory_classifieds') THEN
        CREATE POLICY "Allow public read on theory_classifieds" ON public.theory_classifieds FOR ALL USING (true) WITH CHECK (true);
    END IF;
END $$;
